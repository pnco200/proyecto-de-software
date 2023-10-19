from flask import Blueprint, jsonify, request
from src.core import institutions as institutionsQueries 

api_institution_bp = Blueprint("institution_api", __name__, url_prefix="/api/institutions")

@api_institution_bp.get('/')
def get_institutions():
    params = request.args.to_dict()
    page = None
    per_page = None

    if ('page' in params and 'per_page' not in params) or ('per_page' in params and 'page' not in params):
        return jsonify(message='parametros invalidos'), 400

    if 'page' in params and 'per_page' in params:
        page = int(params['page'])
        per_page = int(params['per_page'])
        institutions = institutionsQueries.list_institutions_paged_api(page=page, per_page=per_page)
    else:
        institutions = institutionsQueries.list_institutions()

    if not institutions:
        return jsonify(data=[], page=page, per_page=per_page, total=0), 200

    institution_list = []

    for institution in institutions.items:
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

    if page and per_page:
        response = {
            'data': institution_list,
            'page': page,
            'per_page': institutions.per_page,
            'total': institutions.total
        }
    else:
        response = {
            'data': institution_list
        }

    return jsonify(response), 200
