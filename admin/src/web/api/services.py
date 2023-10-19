from flask import Blueprint, jsonify, request
from src.core import services as servicesQueries
from src.core.configuration import get_rows_per_page
from src.core.services import get_service_by_keyword_and_type
api_service_bp = Blueprint("service_api", __name__, url_prefix="/api/services/")

@api_service_bp.get('/')
def getServices():
    # Retrieve the required query parameter, "keyword," from the request
    keyword = request.args.get('q')
    print(keyword)
    if keyword is None or keyword == '':
        return jsonify({'error': 'Se requiere el parametro q'}), 400

    # Retrieve the optional query parameters
    service_type = request.args.get('type')
    per_page = request.args.get('per_page', type=int)
    page = request.args.get('page', type=int)

    # Call the function with the retrieved parameters
    services = get_service_by_keyword_and_type(keyword, service_type, per_page, page)

    # Determine the total count of services without pagination
    total_count = len(get_service_by_keyword_and_type(keyword, service_type))

    # Serialize the services within the same function
    service_data = []
    for service in services:
        service_data.append({
            'id': service.id,
            'name': service.name,
            'type': service.type,
            'centers': service.centers,
            'description': service.description,
            'key_words': service.key_words,
            'enabled': service.enabled,
            'institution_id': service.institution_id,
            # Add more fields as needed
        })

    result = {
        'data': service_data,
        'page': page,
        'per_page': per_page,
        'total': total_count  # Total count of services
    }
    return jsonify(result)