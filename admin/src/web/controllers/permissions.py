from flask import Blueprint, render_template, request, flash, redirect,  url_for, session
from src.web.helpers import permissions
from src.web.controllers.users import user_bp
from src.core import rol_permission

permissions_bp = Blueprint('permissions', __name__, url_prefix='/permissions')

@permissions_bp.post('/')
@permissions.has_permission(
    ["institution_show",
    "institution_update",
    "institution_create"
    ],institution)
###Permisos posiblemente necesarios ["institution_create","institution_update"]
def home():
    """
        Para asignar rol en institucion
    """
    institution = request.form.get("Institution_name")
    return render_template("permission/index.html")###To do template



