from flask import Blueprint, jsonify, request
from src.core import service_requests

api_stats_bp = Blueprint("stats_api", __name__, url_prefix="/api/stats/")



@api_stats_bp.get('/requests-institutions')
def get_requests_institutions():
    data = service_requests.get_total_requests_by_institutions()

    parsed_data = []
    for d in data:
        parsed_data.append({
            'Institucion': d[0],
            'Solicitudes': d[1]
        })

    return jsonify(parsed_data)
