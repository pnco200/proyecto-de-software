from flask import Blueprint, jsonify, request
from web.helpers.apivalidations import requires_auth
from src.core.service_requests import get_request_detaile, get_state_by_id
api_user_bp = Blueprint("user_api", __name__, url_prefix="/api/me/")

@api_user_bp.route('/profile')
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
def get_user_requests(user):
    request_id = request.params.get('id')
    if not request_id:
        return jsonify({"error": "Falta el id de la solicitud"}), 400
    service_request = get_request_detaile(request_id)
    if service_request is None:
        return jsonify({"error": "id de solicitud invalido"}), 400
    state = get_state_by_id(service_request.state_id)

    service_request_parsed = {
        "id": service_request.id,
        "name": service_request.name,
        "service_id": service_request.service_id,
        "observations": service_request.observations,
        "inserted_at": service_request.inserted_at,
        "state_name": state.name,
        "state_message": state.state_message,
    }
    
    return jsonify(service_request_parsed), 200