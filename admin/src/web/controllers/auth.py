from flask import Blueprint, render_template, request, flash, redirect,  url_for, session, current_app
from src.core import auth
from src.core.email import email_utils
from src.web.helpers import utils
from src.web.controllers.users import user_bp
from authlib.integrations.flask_client import OAuth
from authlib.integrations.flask_client import OAuthError
from src.web.helpers.auth import oauth
from uuid import uuid4

##DUDAS: PROTEJO PARA QUE SI EL USUARIO QUIERE MANDARLE AL SV EL USERNAME Y LA PASSWORD DE UNA , PARA MI NO PPRQUE CUAL SERIA EL PROBLEMA. DESPUES, SI EL SUPERADMIN CREA EL USER HAY QUE CONFIRMARLO=
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.get('/')
def login():
    """Muestra el form de login"""
    return render_template("auth/login.html")

@auth_bp.route('/google')
def google_login():
    """Me permite loguearme con google
    """
    redirect_uri = url_for('auth.google_auth', _external=True)
    nonce = str(uuid4())
    session['nonce'] = nonce
    return oauth.google.authorize_redirect(redirect_uri, nonce=nonce)

@auth_bp.route('/google/auth')
def google_auth():
    try:
        nonce = session.pop('nonce', None)
        print(nonce)
        token = oauth.google.authorize_access_token(nonce=nonce)
        user_info = oauth.google.parse_id_token(token, nonce=nonce) 
        user = auth.find_user_by_email(user_info["email"])
        if user:
            if not user.is_google:
                flash("El usuario ya existe, pero no fue creado con google.", "error")
                return redirect(url_for('auth.login'))
            else:
                session["user"] = user.id
                flash("La sesion se inicio correctamente.", "success")
                return redirect(url_for('home', _external=True))
        else:
            newUser = auth.create_user_google(name=user_info["given_name"], email=user_info["email"], 
                             password=None, username=user_info["email"], lastname=user_info["family_name"], 
                             is_confirmed=True, is_active=True, is_google=True)
            if newUser:
                flash("El usuario se creo correctamente.", "success")
            else:
                flash("No se pudo crear el usuario.", "error")
            return redirect(url_for('home', _external=True))
    except OAuthError as e:
        flash("La autenticacion fallo: ", 'error')
        return redirect(url_for('auth.login'))


@auth_bp.post('/complete_register')
def complete_register():
    params = request.form
    if not params["token"] or not params["username"] or not params["password"]:
        flash("Falta completar un campo. Vuelva a intentar", "error")
        return redirect(url_for("auth.confirm_email"), token=params["token"])
    existing_user = auth.find_user_by_username(params["username"])
    if existing_user:
        flash("Ese nombre de usuario ya existe.", "error")
        return redirect(url_for("auth.confirm_email"), token=params["token"])
    if auth.update_username_and_password(params["token"],params["username"], params["password"]):
        flash("Informacion actualizada correctamente.", "success")
    else:
        flash("Ocurrio un error inesperado. Vuelva a intentar", "error")

    return redirect(url_for("auth.login"))

@auth_bp.post('/authenticate')
def authenticate():
    """"Me autentica"""
    params = request.form
    user = auth.check_user(params["email"], params["password"])
    if not user:
        flash("Email o clave incorrecta.", "error")
        return redirect(url_for("auth.login"))
    if not user.is_confirmed:
        flash("Su cuenta no esta confirmada. Dirigase a su bandeja de entrada y continue el proceso de registro", "info")
        return redirect(url_for("auth.login"))
    if not user.is_active:
        flash("Su cuenta se encuentra bloqueada o falta completar informacion!", "error")
        return redirect(url_for("auth.login"))
    session["user"] = user.id
    flash("La sesion se inicio correctamente.", "success")
    return redirect(url_for('home', _external=True))


@auth_bp.get('/logout')
def logout():
    """"Me permite cerrar sesion"""
    if session.get("user"):
        del session["user"]
        session.clear()
        flash("La sesion se cerro correctamente.", "info")
    else:
        flash("No hay sesion iniciada.", "info")
    return redirect(url_for("auth.login"))


@auth_bp.get('/confirmemail')
def confirm_email():
    token = request.args.get('token')
    user = auth.confirm_email(token)
    if user:
        if user.password or user.username:
            flash("El correo fue exitosamente confirmado.", "success")
        else:
            flash("El correo fue exitosamente confirmado. Complete la informacion de su cuenta", "success")
            return render_template("auth/complete_register.html", token=token)
    else:
        flash("No se pudo confirmar el correo.", "error")
    return redirect(url_for("auth.login"))


@auth_bp.get('/register')
def register_form():
    """"Muestra el form de registro"""
    return render_template("auth/register.html")

@auth_bp.post('/register')
def register():
    """"Me permite registrarme"""
    params = request.form
    
    if not utils.is_valid_email(params["email"]):
        flash("El email ingresado no es valido.", "error")
        return redirect(url_for("auth.register"))
    
    existing_user = None
    is_superadmin = False
    if "username" in params:
        is_superadmin = True
    if is_superadmin:
        existing_user = auth.find_user_by_email(params["email"]) or auth.find_user_by_username(params["username"])
    else:
        existing_user = auth.find_user_by_email(params["email"])
    if existing_user:
        flash("El mail o nombre de usuario ya esta registrado.", "error")
        return redirect(url_for("auth.register"))
    token = email_utils.send_confirmation_email(params["email"])

    if not token:
        flash("Ocurrio un error al crear el email de confirmacion.", "error")
        return redirect(url_for("auth.register"))
    
    auth.create_user(name=params["name"], email=params["email"], password=params["password"] if is_superadmin else None,username=params["username"] if is_superadmin else None,confirm_token=token, lastname=params["lastname"])
    flash("El usuario se creo correctamente. Revise su bandeja de entrada para terminar el registro.", "success")
    return redirect(url_for("auth.login"))