from functools import wraps
from flask import request, jsonify
from src.core import auth

def requires_auth():
    def decorator(f):

        @wraps(f)
        def decorated_function(*args, **kwargs):
            token = request.headers.get('Authorization')

            if not token:
                return jsonify(error='Falta el token de autorizacion'), 401

            try:
                user_id = int(token)

                user = auth.find_user_by_id(user_id)

                if user is None:
                    return jsonify(error='Token invalido'), 401
            except ValueError:
                return jsonify(error='Formato de token invalido'), 401
            return f(*args, **kwargs)

        return decorated_function
    return decorator

        