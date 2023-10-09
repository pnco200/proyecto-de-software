from flask import Blueprint, render_template, request, flash, redirect,  url_for, session
from src.core import auth
from src.core.email import email_utils
from src.web.helpers import utils

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.get('/')
def login():
    """"Muestra el form de login"""
    return render_template("auth/login.html") ##TO DO!

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
    session["user"] = user.email
    flash("La sesion se inicio correctamente.", "success")
    return redirect(url_for("home"))

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
    
    existing_user = auth.find_user_by_email_or_username(params["email"], params["username"])

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
