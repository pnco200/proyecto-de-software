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

@api_stats_bp.get('/efficient-institutions')
def get_most_efficient():
    data = service_requests.get_top_institutions_less_time_per_request()
    print(data)

    parsed_data = []
    for d in data:
        dias = d[1].total_seconds()//86400
        horas = d[1].total_seconds()%86400 // 3600 
        minutos = d[1].total_seconds()%3600 // 60
        str_time = f'{dias} dias, {horas} horas, {minutos} minutos'
        parsed_data.append({
            'Institucion': d[0],
            'TiempoEnDias': str_time,
            'TiempoTotalSecs': d[1].total_seconds()
        })
    return jsonify(parsed_data)
