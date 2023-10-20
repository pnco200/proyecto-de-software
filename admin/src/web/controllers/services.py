from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from src.core import services
from src.web.helpers.utils import current_selected_institution
from src.web.helpers import permissions
from src.core.rol_permission import get_role_id_by_name, get_roles_for_user

service_bp = Blueprint('services', __name__, url_prefix='/services')


@service_bp.get("/")
@permissions.permission_required_in_Institution(["service_index"])
def list_services():
    page = request.args.get('page', type=int, default=1)
    current_institution_id = current_selected_institution()
    list = services.list_services_paged_by_institution(page, current_institution_id)
    return render_template("services/index.html", services=list, page=page)

@service_bp.get("/config/<int:service_id>")
@permissions.permission_required_in_Institution(["service_show"])
def config_service(service_id):
    service = services.get_service(service_id)
    institution_id = current_selected_institution()
    user_id = session.get('user')
    
    is_operator = False
    operator_role_id = get_role_id_by_name("Operator")
    user_roles = get_roles_for_user(user_id, institution_id)
    
    is_operator = len(user_roles) == 1 and operator_role_id in user_roles

    return render_template("services/config.html", service=service, is_operator=is_operator)

@service_bp.get("/create")
@permissions.permission_required_in_Institution(["service_create"])
def create_service_form():
    """
        Muestra el form de creacion de servicios
    """
    return render_template("services/create.html")

@service_bp.post("/create")
@permissions.permission_required_in_Institution(["service_create"])
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

    current_institution_id = current_selected_institution()

          
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
@permissions.permission_required_in_Institution(["service_destroy"])
def delete_service(service_id):
    """
        Me permite eliminar un servicio
    """
    services.delete_service(service_id)
    flash("El servicio fue eliminado correctamente.", "success")
    return redirect(url_for('services.list_services', ))

@service_bp.get("/update/<int:service_id>")
@permissions.permission_required_in_Institution(["service_update"])
def update_service_form(service_id):
    """
        Muestra el form de actualizacion de servicios
    """
    service = services.get_service(service_id)
    return render_template("services/update.html", service=service)

@service_bp.post("/update/<int:service_id>")
@permissions.permission_required_in_Institution(["service_update"])
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