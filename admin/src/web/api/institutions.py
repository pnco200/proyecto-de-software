from flask import Blueprint, jsonify, request
from src.core import institutions as institutionsQueries 
from src.core.configuration import get_rows_per_page
api_institution_bp = Blueprint("institution_api", __name__, url_prefix="/api/institutions")

@api_institution_bp.get('/')
def get_institutions():
    params = request.args.to_dict()
    page = 1
    per_page = None

    try:
        if 'page' in params :
            page = int(params['page'])
        if 'per_page' in params:
            per_page = int(params['per_page'])
    except ValueError:
        return jsonify(error='Parametros Invalidos'), 400
    
    if not per_page:
        per_page = get_rows_per_page()

    paginated_institutions = institutionsQueries.list_institutions_paged_api(page=page, per_page=per_page)
    total_institutions_count = len(institutionsQueries.list_institutions())

    if not paginated_institutions:
        return jsonify(data=[], page=page, per_page=per_page, total=total_institutions_count), 200

    institution_list = []

    for institution in paginated_institutions:
        institution_data = {
            'id': institution.id,
            'name': institution.name,
            'information': institution.information,
            'address': institution.address,
            'localization': institution.localization,
            'web': institution.web,
            'keywords': institution.keywords,
            'attention_time': institution.attention_time,
            'contact': institution.contact,
            'is_active': institution.is_active
        }
        institution_list.append(institution_data)


    response = {
        'data': institution_list,
        'page': page,
        'per_page': per_page,
        'total': total_institutions_count
    }

    return jsonify(response), 200

@api_institution_bp.get('/<int:institution_id>')
def get_institution_by_id(institution_id):
    if not institution_id:
        return jsonify({'error': 'Parametro Invalido'}), 400

    institution = institutionsQueries.get_institution_by_id(id=institution_id)


    if not institution:
        return {}, 200
    institution_data = {
        'id': institution.id,
        'name': institution.name,
        'information': institution.information,
        'address': institution.address,
        'localization': institution.localization,
        'web': institution.web,
        'keywords': institution.keywords,
        'attention_time': institution.attention_time,
        'contact': institution.contact,
        'is_active': institution.is_active
    }
    return jsonify(institution_data), 200