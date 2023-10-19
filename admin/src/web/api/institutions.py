from flask import Blueprint, jsonify, request
from src.core.institutions import list_institutions_paged_api

api_institution_bp = Blueprint("institution_api", __name__, url_prefix="/api/institutions")

@api_institution_bp.get('/')
def get_institutions():
    page = int(request.args.get('page'))
    per_page = int(request.args.get('per_page'))
    
    

    institutions = list_institutions_paged_api(page=page, per_page=per_page)
    
    if not institutions:
        return jsonify(data=[], page=page, per_page=per_page, total=0), 200

    institution_list = []

    for institution in institutions.items:
        institution_data = {
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
        'per_page': institutions.per_page,
        'total': institutions.total
    }

    return jsonify(response), 200
