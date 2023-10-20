from flask import Blueprint, render_template, request, flash, redirect,  url_for
from src.core import configuration
from src.core.email import email_utils
from src.web.helpers import utils
from src.web.helpers import permissions

config_bp = Blueprint('configuration', __name__, url_prefix='/config')

@config_bp.get('/')
@permissions.has_permission(['config_show'])
def index():
    config = configuration.get_configuration()
    return render_template('configuration/index.html', configuration=config)

@config_bp.post('/update')
@permissions.has_permission(['config_update'])
def update_configuration():
    """"Actualiza la configuracion del sitio"""
    rows_per_page = request.form.get('rows_per_page')
    contact_information = request.form.get('contact_information')
    is_maintenance = True if request.form.get('is_maintenance') == 'on' else False
   
    maintenance_message = request.form.get('maintenance_message')
    if not utils.is_valid_length(contact_information, 50):
        flash("La informacion de contacto no debe superar los 50 caracteres!", "error")
        return redirect(url_for("configuration.index"))
    if not utils.is_valid_length(maintenance_message, 255):
        flash("El mensaje de mantenimiento no debe superar los 255 caracteres!", "error")
        return redirect(url_for("configuration.index"))
    result = configuration.update_configuration(
        rows_per_page=rows_per_page,
        contact_information=contact_information,
        is_maintenance=is_maintenance,
        maintenance_message=maintenance_message
    )
    if(result):
        flash("Informacion actualizada exitosamente", "success")
    else:
        flash("Ocurrio un error inesperado al actualizar la informacion de configuracion", "error")
    return redirect(url_for("configuration.index"))
