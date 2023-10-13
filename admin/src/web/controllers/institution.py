from flask import Blueprint, render_template, session, abort, request, url_for, redirect, flash
from src.core import institutions
from src.web.helpers.utils import is_valid_length, is_valid_email

institution_bp = Blueprint('institution', __name__, url_prefix='/institution')

@institution_bp.get('/')
def home():
    """"Muestra un listado de todas las instituciones"""
    page = request.args.get('page', type=int, default=1)
    institutionsList = institutions.list_institutions_paged(page)
    print(institutionsList)
    return render_template("institutions/index.html", institutions=institutionsList, page=page)
    
@institution_bp.get('/register')
def register_form():
    """"Muestra el form de registro"""
    return render_template("institutions/register.html")

@institution_bp.post('/register')
def register():
    """Permite registrar una institucion"""
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
    


