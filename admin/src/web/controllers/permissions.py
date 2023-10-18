from flask import Blueprint, render_template, request, flash, redirect,  url_for, session
from src.web.helpers import permissions
from src.web.controllers.users import user_bp
from src.core import rol_permission

permissions_bp = Blueprint('permissions', __name__, url_prefix='/permissions')

@permissions_bp.post('/')
@permissions.permission_required_in_Institution(
    ["institution_show",
    "institution_update",
    "institution_create"
    ], request)
###Permisos posiblemente necesarios ["institution_create","institution_update"]
def home():
    """
        Para asignar rol en institucion
    """
    ## Tomo el insituto por nombre segun lo elegido en el form o lo pasado como parametro
    institution_name = request.form.get("Institution_name")
    return render_template("permission/index.html")###To do template



###hacer controladores que necesiten permisos(?)