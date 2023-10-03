from flask import Blueprint, render_template, session, abort
from src.web.helpers.auth import login_required

user_bp = Blueprint('user', __name__, url_prefix='/users')

@user_bp.get('/')
@login_required
#@check("permiso o rol?")
def home():
    """"Muestra un listado de los usuarios si el usuario esta logeado"""
    return render_template("users/index.html")


