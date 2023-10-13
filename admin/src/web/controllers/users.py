from flask import Blueprint, render_template, request
from src.web.helpers.auth import login_required, has_permission
from src.core import auth
user_bp = Blueprint('user', __name__, url_prefix='/users')

@user_bp.get('/')
@login_required
@has_permission(["user_index"])
def home():
    ##Ver de hacer tablas de permisos
    """"Muestra un listado de los usuarios si el usuario esta logeado"""
    page = request.args.get('page', type=int, default=1)
    users = auth.list_users_paged(page)
    return render_template("users/index.html", users=users, page=page)

