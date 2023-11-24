from flask import Blueprint, jsonify, request
from src.core import services as servicesQueries
from src.core.configuration import get_rows_per_page

api_service_bp = Blueprint("service_api", __name__, url_prefix="/api/services")



@api_service_bp.get('/search')
def getServices():
    keyword = request.args.get('q')
    if keyword is None or keyword == '':
        keyword=None
    service_type = request.args.get('type') 
    if service_type != "ANALISIS" and service_type != "CONSULTORIA" and service_type != "DESARROLLO":
        service_type = None
    per_page = request.args.get('per_page', get_rows_per_page(), type=int)
    page = request.args.get('page', 1, type=int)
    queryRes = servicesQueries.get_service_by_keyword_and_type(keyword=keyword, service_type=service_type, per_page=per_page, page=page)

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
            'institution_name': service.institution.name,
            'institution_id': service.institution.id,
        })

    result = {
        'data': service_data,
        'page': page,
        'per_page': per_page if per_page else get_rows_per_page(),
        'total': total_count 
    }

    return jsonify(result)

@api_service_bp.get('/<int:service_id>')
def get_service_by_id(service_id):
    if not service_id:
        return jsonify({'error': 'Parametro Invalido'}), 400

    service = servicesQueries.get_service(service_id)
    if service:
        result = {
                'id': service.id,
                'name': service.name,
                'type': service.type.value,
                'centers': service.centers,
                'description': service.description,
                'key_words': service.key_words,
                'enabled': service.enabled,
                'institution_id': service.institution_id,
            }
        return jsonify(result), 200
    else:
        return jsonify(), 204
    
@api_service_bp.get('/types')
def get_service_types():
    service_types = servicesQueries.get_service_types()
    return jsonify(service_types), 200

