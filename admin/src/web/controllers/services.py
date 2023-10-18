from flask import Blueprint, render_template, request, redirect, url_for, flash
from src.core import services
from src.web.helpers.utils import current_selected_institution
service_bp = Blueprint('services', __name__, url_prefix='/services')


@service_bp.get("/")
def list_services():
    page = request.args.get('page', type=int, default=1)
    current_institution_id = current_selected_institution(request)
    list = services.list_services_paged_by_institution(page, current_institution_id)
    return render_template("services/index.html", services=list, page=page)

@service_bp.get("/config/<int:service_id>")
def config_service(service_id):
    service = services.get_service(service_id)
    return render_template("services/config.html", service=service)

@service_bp.get("/create")
def create_service_form():
    """
        Muestra el form de creacion de servicios
    """
    return render_template("services/create.html")

@service_bp.post("/create")
def create_service():
    """
        Me permite crear un servicio
    """
    key_words_string = request.form.get('key_words')
    if key_words_string:
        key_words_array = [word.strip() for word in key_words_string.split(",")]
    else:
        key_words_array = []
    centers_string = request.form.get('centers')
    if centers_string:
        centers_array = [center.strip() for center in centers_string.split(",")]
    else:
        centers_array = []    
    name = request.form.get('name')
    description = request.form.get('description')
    service_type = request.form.get('type')

    current_institution_id = current_selected_institution(request)

          
    params = {
        'name': name,
        'description': description,
        'key_words': key_words_array,
        'centers': centers_array,
        'type': service_type,
        'institution_id': current_institution_id
    }
    services.create_service(**params)
    flash("El servicio fue creado correctamente.", "success")
    return redirect(url_for('services.list_services'))

@service_bp.post("/delete/<int:service_id>")
def delete_service(service_id):
    """
        Me permite eliminar un servicio
    """
    services.delete_service(service_id)
    flash("El servicio fue eliminado correctamente.", "error")
    return redirect(url_for('services.list_services'))

@service_bp.get("/update/<int:service_id>")
def update_service_form(service_id):
    """
        Muestra el form de actualizacion de servicios
    """
    service = services.get_service(service_id)
    return render_template("services/update.html", service=service)

@service_bp.post("/update/<int:service_id>")
def update_service(service_id):
    """
        Me permite actualizar un servicio
    """
    key_words_string = request.form.get('key_words')
    if key_words_string:
        key_words_array = [word.strip() for word in key_words_string.split(",")]
    else:
        key_words_array = []
    centers_string = request.form.get('centers')
    if centers_string:
        centers_array = [center.strip() for center in centers_string.split(",")]
    else:
        centers_array = []    
    name = request.form.get('name')
    description = request.form.get('description')
    service_type = request.form.get('type')
    enabled = request.form.get('enabled') == 'True'

    params = {
        'name': name,
        'description': description,
        'key_words': key_words_array,
        'centers': centers_array,
        'type': service_type,
        'enabled': enabled
    }
    services.update_service(service_id, **params)
    flash("El servicio fue actualizado correctamente.", "success")
    return redirect(url_for('services.list_services'))