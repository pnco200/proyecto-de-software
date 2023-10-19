from flask import Blueprint, jsonify, request
from src.core import auth 

api_auth_bp = Blueprint("auth_api", __name__, url_prefix="/api/auth")

@api_auth_bp.post('/')
def login():
    params = request.json
    if ('user' not in params or 'password' not in params):
        return jsonify(error='Parametros invalidos'), 400
    print(params["user"], params["password"])
    user = auth.check_user(params["user"], params["password"])
    if user:
        return jsonify(result="success"), 200
    else:
        return jsonify(result="fail"), 400