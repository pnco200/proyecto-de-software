from flask import Blueprint, render_template, session, abort, request, url_for, redirect, flash, make_response, request
from src.core import institutions
from src.web.helpers.utils import is_valid_length, is_valid_email
from src.web.helpers import permissions
from src.web.helpers.auth import generate_csrf_token, check_csrf_token

institution_bp = Blueprint('institution', __name__, url_prefix='/institution')

@institution_bp.get('/')
@permissions.has_permission(["institution_index"])
def home():
    """"Muestra un listado de todas las instituciones"""
    page = request.args.get('page', type=int, default=1)
    institutionsList = institutions.list_institutions_paged(page)
    print(institutionsList)
    return render_template("institutions/index.html", institutions=institutionsList, page=page)
    
@institution_bp.get('/register')
@permissions.has_permission(["institution_create"])
def register_form():
    """"Muestra el form de registro"""
    csrf_token = generate_csrf_token()
    return render_template("institutions/register.html", csrf_token=csrf_token)

@institution_bp.route('/confirm_delete/<int:institution_id>', methods=['GET', 'POST'])
@permissions.has_permission(["institution_destroy"])
def confirm_delete(institution_id):
    """Permite confirmar la eliminacion de una institucion si el metodo es GET,
        si es POST elimina la institucion
    Args:
        institution_id (int): id de la institucion a eliminar
    Returns:
        home: si se elimino correctamente o incorrectamente
        confirm_delete: si se quiere confirmar la eliminacion
    """
    
    if request.method == 'POST':
        if not check_csrf_token(request.form):
            flash("Token CSRF invalido", "error")
        
        institution = institutions.delete_institution(institution_id)
        if institution:
            flash("La institucion se ha eliminado correctamente.", "success")
            return redirect(url_for("institution.home"))
        else:
            flash("No se ha podido eliminar la institucion.", "error")
            return redirect(url_for("institution.home"))
    csrf_token = generate_csrf_token()
    return render_template('institutions/confirm_delete.html', institution_id=institution_id, csrf_token=csrf_token)

@institution_bp.post('/select_institution')
@permissions.has_permission(["institution_show"]) #Utilizamos el show para que puedan ver el select de la navbar de sus instituciones pero NO todo el listado de instituciones
def select_institution():
    """Cambia la institucion seleccionada en la barra de navegacion"""
    selected_institution = request.form.get('selected_institution')
    if selected_institution:
        response = make_response(redirect(url_for("home")))
        response.set_cookie('selectedInstitution', selected_institution)
    return response

@institution_bp.post('/register')
@permissions.has_permission(["institution_create"])
def register():
    """Permite registrar una institucion
    """
    params = request.form
    is_active = True if params.get('is_active') == 'on' else False
    
    required_params = ["name", "information", "address", "localization", "web", "keywords", "attention_time", "contact"]

    for param in required_params:
        if param not in params:
            flash(f"El parámetro '{param}' es obligatorio", "error")
            return redirect(url_for("institution.register_form"))
    
    if not is_valid_length(params["name"], 50):
        flash("El nombre excede los 50 caracteres.", "error")
        return redirect(url_for("institution.register_form"))

    if not is_valid_length(params["information"], 250):
        flash("La informacion excede los 250 caracteres.", "error")
        return redirect(url_for("institution.register_form"))
    
    if not is_valid_length(params["address"], 250):
        flash("La direccion excede los 250 caracteres.", "error")
        return redirect(url_for("institution.register_form"))
    
    if not is_valid_length(params["localization"], 50):
        flash("La localizacion excede los 50 caracteres.", "error")
        return redirect(url_for("institution.register_form"))
    
    if not is_valid_length(params["web"], 250):
        flash("El sitio web excede los 250 caracteres.", "error")
        return redirect(url_for("institution.register_form"))
    
    if not is_valid_length(params["keywords"], 500):
        flash("Las palabras clave excede los 500 caracteres.", "error")
        return redirect(url_for("institution.register_form"))
    
    if not is_valid_length(params["attention_time"], 250):
        flash("El horario de atencion excede los 250 caracteres.", "error")
        return redirect(url_for("institution.register_form"))
    
    if not is_valid_length(params["contact"], 250):
        flash("El contacto excede los 250 caracteres.", "error")
        return redirect(url_for("institution.register_form"))
    
    if institutions.institution_exists(params["name"]):
        flash("La institucion ya existe.", "error")
        return redirect(url_for("institution.register_form"))

    institution = institutions.create_institution(name=params["name"], 
                                    information=params["information"], 
                                    address=params["address"], 
                                    localization=params["localization"], 
                                    web=params["web"], 
                                    keywords=params["keywords"], 
                                    attention_time=params["attention_time"], 
                                    contact=params["contact"], 
                                    is_active=is_active)
    
    if(institution):
        flash("La institucion se ha registrado correctamente.", "success")
        return redirect(url_for("institution.register_form"))
    else:
        flash("No se ha podido registrar la institucion.", "error")
        return redirect(url_for("institution.register_form"))
    
@institution_bp.get('/update/<int:institution_id>')
@permissions.has_permission(["institution_update"])
def getInstitution(institution_id):
    """Permite obtener una institucion por id para actualizarla

    Args:
        institution_id (int): id de la institucion a obtener

    Returns:
        template: template de actualizacion de institucion 
    """
    csrf_token = generate_csrf_token()

    institutionToUpdate = institutions.get_institution_by_id(institution_id)
    print(institutionToUpdate.is_active)
    return render_template("institutions/update.html", institution=institutionToUpdate, csrf_token=csrf_token)

@institution_bp.post('/update/<int:institution_id>')
@permissions.has_permission(["institution_update"])
def updateInstitution(institution_id):
    """Permite actualizar una institucion

    Args:
        institution_id (int): id de la institucion a actualizar

    """
    params = request.form
    if not check_csrf_token(params):
        flash("Token CSRF invalido", "error")
        return redirect(url_for("institution.home"))

    is_active = True if params.get('is_active') == 'on' else False
    
    required_params = ["name", "information", "address", "localization", "web", "keywords", "attention_time", "contact"]

    for param in required_params:
        if param not in params:
            flash(f"El parámetro '{param}' es obligatorio", "error")
            return redirect(url_for("institution.register_form"))
    
    if not is_valid_length(params["name"], 50):
        flash("El nombre excede los 50 caracteres.", "error")
        return redirect(url_for("institution.register_form"))

    if not is_valid_length(params["information"], 250):
        flash("La informacion excede los 250 caracteres.", "error")
        return redirect(url_for("institution.register_form"))
    
    if not is_valid_length(params["address"], 250):
        flash("La direccion excede los 250 caracteres.", "error")
        return redirect(url_for("institution.register_form"))
    
    if not is_valid_length(params["localization"], 50):
        flash("La localizacion excede los 50 caracteres.", "error")
        return redirect(url_for("institution.register_form"))
    
    if not is_valid_length(params["web"], 250):
        flash("El sitio web excede los 250 caracteres.", "error")
        return redirect(url_for("institution.register_form"))
    
    if not is_valid_length(params["keywords"], 500):
        flash("Las palabras clave excede los 500 caracteres.", "error")
        return redirect(url_for("institution.register_form"))
    
    if not is_valid_length(params["attention_time"], 250):
        flash("El horario de atencion excede los 250 caracteres.", "error")
        return redirect(url_for("institution.register_form"))
    
    if not is_valid_length(params["contact"], 250):
        flash("El contacto excede los 250 caracteres.", "error")
        return redirect(url_for("institution.register_form"))
    
    institution = institutions.update_institution(
                                    id=institution_id,
                                    name=params["name"], 
                                    information=params["information"], 
                                    address=params["address"], 
                                    localization=params["localization"], 
                                    web=params["web"], 
                                    keywords=params["keywords"], 
                                    attention_time=params["attention_time"], 
                                    contact=params["contact"], 
                                    is_active=is_active)
    
    if(institution):
        flash("La institucion se ha actualizado correctamente.", "success")
        return redirect(url_for("institution.home"))
    else:
        flash("No se ha podido actualizar la institucion.", "error")
        return redirect(url_for("institution.home"))
    
    