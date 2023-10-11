from flask import Blueprint, render_template, session, abort, request, url_for, redirect, flash
from src.core import institutions
from src.web.helpers.utils import is_valid_length, is_valid_email

institution_bp = Blueprint('institution', __name__, url_prefix='/institution')

@institution_bp.get('/')
def home():
    """"Muestra un listado de todas las instituciones"""
    listadoInstituciones = institutions.list_institutions()
    return render_template("institutions/index.html", institutions=listadoInstituciones)
    
@institution_bp.get('/register')
def register_form():
    """"Muestra el form de registro"""
    return render_template("institutions/register.html")

@institution_bp.post('/register')
def register():
    params = request.form
    
    print(params)
    return redirect(url_for("home"))