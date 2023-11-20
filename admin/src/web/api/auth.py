from flask import Blueprint, jsonify, request
from src.core import auth
from flask_jwt_extended import create_access_token


api_auth_bp = Blueprint("auth_api", __name__, url_prefix="/api/auth")

@api_auth_bp.post('/')
def login():
    params = request.json
    if ('user' not in params or 'password' not in params):
        return jsonify(error='Parametros invalidos'), 400
    user = auth.check_user(params["user"], params["password"])
    if user and user.is_active and user.is_confirmed:
        access_token = create_access_token(identity=user.id)
        return jsonify(result=access_token), 200
    else:
        return jsonify(result="fail"), 400