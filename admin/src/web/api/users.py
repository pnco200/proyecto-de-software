from flask import Blueprint, jsonify, request
from web.helpers.apivalidations import requires_auth
from src.core.configuration import get_rows_per_page
from src.core import service_requests
api_user_bp = Blueprint("user_api", __name__, url_prefix="/api/me/")

@api_user_bp.get('/profile')
@requires_auth()
def get_user_profile(user):
    profile = {
        "name": user.name,
        "email": user.email,
        "id": user.id,
        "lastname": user.lastname,
        "username": user.username,
    }
    return jsonify(profile), 200


@api_user_bp.get('/requests')
@requires_auth()
def get_requests_paginated(user):
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

    paginated_requests = service_requests.list_requests_paged_by_user(page=page, per_page=per_page, user_id=user.id)
    total_count = len(service_requests.list_all_requests_by_user(user_id=user.id))
    final_list = []

    for req in paginated_requests:
        request_data = {
            "name": req.ServiceRequest.name,
            "creation_date": req.ServiceRequest.inserted_at,
            "close_date": req.ServiceRequest.closed_at,
            "status": req.service_state_alias.name,
            "observations": req.ServiceRequest.observations
        }
        final_list.append(request_data)


    response = {
        'data': final_list,
        'page': page,
        'per_page': per_page,
        'total': total_count
    }
    return jsonify(response), 200

@api_user_bp.post('/requests/<int:service_request_id>/notes')
@requires_auth()
def add_note_to_request(user, service_request_id):
    text = request.json["text"]
    if not text:
        return jsonify(error='Parametros Invalidos'), 400
    text_added = service_requests.create_message_request(service_request_id=service_request_id, user_id=user.id, msg_content=text)
    if text_added:
        return jsonify(), 200
    else:
        return jsonify(error='ID no encontrada'), 404