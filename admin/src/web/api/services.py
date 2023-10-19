from flask import Blueprint, jsonify, request
from src.core import services as servicesQueries
from src.core.configuration import get_rows_per_page

from src.core.services import get_service_by_keyword_and_type
api_service_bp = Blueprint("service_api", __name__, url_prefix="/api/services/")



@api_service_bp.get('/search')
def getServices():
    print(request.args.get('type'))
    keyword = request.args.get('q')
    if keyword is None or keyword == '':
        return jsonify({'error': 'Se requiere el parametro q'}), 400

    service_type = request.args.get('type')
    per_page = request.args.get('per_page', get_rows_per_page(), type=int)
    page = request.args.get('page', 1, type=int)


    queryRes = get_service_by_keyword_and_type(keyword=keyword, service_type=service_type, per_page=per_page, page=page)

    if(queryRes == False):
        return jsonify({'error': 'Parametros Invalidos'}), 400
    services = queryRes[0]
    total_count = queryRes[1]

    service_data = []
    for service in services:
        service_data.append({
            'id': service.id,
            'name': service.name,
            'type': service.type.value,
            'centers': service.centers,
            'description': service.description,
            'key_words': service.key_words,
            'enabled': service.enabled,
            'institution_id': service.institution_id,
        })

    result = {
        'data': service_data,
        'page': page,
        'per_page': per_page if per_page else get_rows_per_page(),
        'total': total_count 
    }

    return jsonify(result)