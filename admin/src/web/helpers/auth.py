from functools import wraps
from flask import session, abort, request, jsonify
from authlib.integrations.flask_client import OAuth
from src.core import auth

oauth = OAuth()

oauth.register(
    name='google',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'openid email profile'
    }
)

def is_authenticated(session):
    return session.get("user") is not None

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not is_authenticated(session):
            return abort(401)
        return f(*args, **kwargs)
    return decorated_function
        