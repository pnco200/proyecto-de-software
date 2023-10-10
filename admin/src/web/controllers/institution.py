from flask import Blueprint, render_template, session, abort
from src.core import institutions

institution_bp = Blueprint('institution', __name__, url_prefix='/institution')

@institution_bp.get('/')
def home():
    """"Muestra un listado de todas las instituciones"""
    listadoInstituciones = institutions.list_institutions()
    return render_template("institutions/index.html", institutions=listadoInstituciones)
    
