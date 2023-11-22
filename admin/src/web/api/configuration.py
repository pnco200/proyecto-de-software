from flask import Blueprint, jsonify, request
from src.core import configuration


api_configuration_bp = Blueprint("configuration_api", __name__, url_prefix="/api/configuration")

@api_configuration_bp.get('/getconfig')
def getConfiguration():
    """Devuelve la configuracion actual del sitio

    Returns:
        Configuration: Devuelve un objeto Configuration(rows_per_page, contact_information, is_maintenance, maintenance_message)
    """
    data = configuration.get_configuration()
    parsedData = {
        "rows_per_page": data.rows_per_page,
        "contact_information": data.contact_information,
        "is_maintenance": data.is_maintenance,
        "maintenance_message": data.maintenance_message
    }

    return jsonify(parsedData), 200
    