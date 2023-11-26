from flask import Blueprint, jsonify, request
from web.helpers.apivalidations import requires_auth
from src.core.configuration import get_rows_per_page
from src.core import service_requests
from src.core import auth
from src.core.service_requests import get_request_detaile, get_state_by_id, create_service_request
from flask_jwt_extended import jwt_required,get_jwt_identity
from datetime import datetime
api_user_bp = Blueprint("user_api", __name__, url_prefix="/api/me/")

@api_user_bp.get('/profile')
@jwt_required()
def get_user_profile():
    user_id = get_jwt_identity()
    user = auth.find_user_by_id(user_id)
    profile = {
        "name": user.name,
        "email": user.email,
        "id": user.id,
        "lastname": user.lastname,
        "username": user.username,
    }
    return jsonify(profile), 200

@api_user_bp.get('/requests/<int:service_request_id>')
@jwt_required()
def get_user_requests(service_request_id):
    user_id = get_jwt_identity()
    user = auth.find_user_by_id(user_id)
    query = get_request_detaile(service_request_id)
    if not query:
        return jsonify({"error": "ID de solicitud inválido"}), 400

    service_request = query.ServiceRequest
    service_service = query.service_alias
    service_state = query.request_state
    fecha = service_request.inserted_at.strftime("%Y-%m-%d %H:%M:%S")
    service_request_parsed = {
        "id": service_request.id,
        "user_id" : service_request.user_id,
        "service_id": service_request.service_id,
        "observations": service_request.observations,
        "inserted_at": fecha,
        "status": service_state.name,
        "file":service_request.archive,
        "state_message": service_state.state_message,
    }
    
    return jsonify(service_request_parsed), 200


@api_user_bp.get('/requests-paginated')
@jwt_required()
def get_requests_paginated():
    user_id = get_jwt_identity()
    user = auth.find_user_by_id(user_id)
    
    params = request.args.to_dict()
    print(params)
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
            "id": req.ServiceRequest.id,
            "user_id" : req.ServiceRequest.user_id,
            "service_id": req.ServiceRequest.service_id, #Añadido para poder desde el portal solicitar la informacion de la solicitud especifica
            "name": req.ServiceRequest.name,
            "creation_date":req.ServiceRequest.inserted_at ,
            "status": req.service_state_alias.name,
            "observations": req.ServiceRequest.observations
        }
        if('status' in params and params['status']):
            if(params['status']==request_data['status']):
                final_list.append(request_data)       
        else:
            final_list.append(request_data)
            
    
    if('order' in params):         
        final_list = sorted(final_list, key=lambda x: x['creation_date'])
    for fecha in final_list:
        fecha['creation_date']= fecha['creation_date'].strftime("%Y-%m-%d %H:%M:%S")
    
    response = { 
        'data': final_list,
        'page': page,
        'per_page': per_page,
        'total': total_count
    }
    return jsonify(response), 200

@api_user_bp.post('/created-request')
@jwt_required()
def create_request():
    user_id = get_jwt_identity()
    user = auth.find_user_by_id(user_id)
    data = request.json
    if "service_id" not in data or "description" not in data:
        
        return jsonify(error='Parametros Invalidos'), 400

    service_id = data["service_id"]
    description = data["description"]

    resulting_request = create_service_request(service_id=service_id, user_id=user.id, observations=description, archive=data["file"])
    
    if not resulting_request:
        
        return jsonify(error='ID de servicio invalido'), 400
    state = service_requests.get_state_by_id(resulting_request.state_id)
    fecha = resulting_request.inserted_at.strftime("%Y-%m-%d %H:%M:%S")

    response = {
        "id": resulting_request.id,
        "service_id": resulting_request.service_id,
        "user_id": resulting_request.user_id,
        "observations": resulting_request.observations,
        "inserted_at": fecha,
        "status":state[0].name,
    }
    print(response)
    return jsonify(response), 201

@api_user_bp.post('/requests/<int:service_request_id>/add-notes')
@jwt_required()
def add_note_to_request(service_request_id):
    user_id = get_jwt_identity()
    user = auth.find_user_by_id(user_id)
    text = request.json["text"]
    if not text:
        return jsonify(error='Parametros Invalidos'), 400
    text_added = service_requests.create_message_request(service_request_id=service_request_id, user_id=user.id, msg_content=text)
    if text_added:
        res = {
            "id": service_request_id,
            "text": text
        }
        return jsonify(res), 201
    else:
        return jsonify(error='ID no encontrada'), 404

@api_user_bp.get('/request/<int:request_id>/notes')
@jwt_required()
def get_request_notes(request_id):
    try:
        user_id = get_jwt_identity()
        user = auth.find_user_by_id(user_id)
        if not user:
            return jsonify(error='Usuario no encontrado'), 404

        user_and_msgs = service_requests.get_request_msgs(request_id)
        
        final_list = []

        if user_and_msgs:
            for msg in user_and_msgs:
                response = {
                    "id": msg.id,
                    "user_id": msg.user_id,
                    "service_id": msg.service_request_id,
                    "creation_date": msg.inserted_at,
                    "content": msg.msg_content
                }
                final_list.append(response)

            final_list = sorted(final_list, key=lambda x: x['creation_date'])
            response = {'data': final_list,'id':user_id}
            print(final_list)
            return jsonify(response), 200
        else:
            return jsonify(error='Mensajes no encontrados'), 404
    except Exception as e:
        # Log the exception for debugging purposes
        print(f"Error in get_request_notes: {str(e)}")
        return jsonify(error='Error interno del servidor'), 500
