from flask import Blueprint, render_template, session, abort
from src.web.helpers.auth import login_required
from src.core import auth
user_bp = Blueprint('user', __name__, url_prefix='/users')

@user_bp.get('/')
@login_required
#@check("permiso o rol?")
def home():
    """"Muestra un listado de los usuarios si el usuario esta logeado"""
    users = auth.list_users()
    return render_template("users/index.html", users=users)


