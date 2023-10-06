from flask import Blueprint, render_template, request, flash, redirect,  url_for, session
from src.core import auth
from src.core.email import email_utils

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.get('/')
def login():
    """"Muestra el form de login"""
    return render_template("login.html") ##TO DO!

@auth_bp.post('/authenticate')
def authenticate():
    """"Me autentica"""
    params = request.form
    user = auth.check_user(params["email"], params["password"])
    if not user:
        flash("Email o clave incorrecta.", "error")
        return redirect(url_for("auth.login"))
    session["user"] = user.email
    flash("La sesion se inicio correctamente, success")
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

@auth_bp.get('/register')
def register_form():
    """"Muestra el form de registro"""
    return render_template("register.html")

@auth_bp.post('/register')
def register():
    """"Me permite registrarme"""
    params = request.form

    existing_user = auth.find_user_by_email(params["email"])

    if existing_user:
        flash("El usuario ya existe.", "error")
        return redirect(url_for("auth.register"))
    
    auth.create_user(**params)
    flash("El usuario se creo correctamente.", "success")
    email_utils.send_email("Prueba",[params["email"]],"Email de confirmacion")
    return redirect(url_for("auth.login"))
