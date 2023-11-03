from flask import Blueprint, render_template, request, flash, redirect,  url_for, session, current_app
from src.core import auth
from src.core.email import email_utils
from src.web.helpers import utils
from src.web.controllers.users import user_bp
from authlib.integrations.flask_client import OAuth
from authlib.integrations.flask_client import OAuthError
from src.web.helpers.auth import oauth

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
    return oauth.google.authorize_redirect(redirect_uri)

@auth_bp.route('/google/auth')
def google_auth():
    try:
        token = oauth.google.authorize_access_token()
        user_info = oauth.google.parse_id_token(token)
        # Handle user authentication and session management here
        # Example: check if the user exists in your database and create a session
        return redirect(url_for('home', _external=True))
    except OAuthError as e:
        # Handle OAuth error, such as an invalid token
        flash("OAuth authentication failed: " + str(e), 'error')
        return redirect(url_for('auth.login'))

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
        flash("Su cuenta se encuentra bloqueada!", "error")
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
        flash("El correo fue exitosamente confirmado.", "success")
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
    
    existing_user = auth.find_user_by_email(params["email"]) or auth.find_user_by_username(params["username"])

    if existing_user:
        flash("El mail o nombre de usuario ya esta registrado.", "error")
        return redirect(url_for("auth.register"))
    token = email_utils.send_confirmation_email(params["email"])

    if not token:
        flash("Ocurrio un error al crear el email de confirmacion.", "error")
        return redirect(url_for("auth.register"))
    
    auth.create_user(name=params["name"], email=params["email"], password=params["password"],username=params["username"],confirm_token=token, lastname=params["lastname"])
    flash("El usuario se creo correctamente. Revise su bandeja de entrada para terminar el registro.", "success")
    return redirect(url_for("auth.login"))
