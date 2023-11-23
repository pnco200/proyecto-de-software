from functools import wraps
from flask import session, abort, request, jsonify
from authlib.integrations.flask_client import OAuth
from src.core import auth
import os
oauth = OAuth()

oauth.register(
    name='google',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'openid email profile'
    }
)

def generate_csrf_token():
    if 'csrf_token' not in session:
        session['csrf_token'] = os.urandom(32).hex()
    return session['csrf_token']

def check_csrf_token(params):
    if 'csrf_token' not in session or params.get('csrf_token') != session['csrf_token']:
        return False
    session.pop('csrf_token', None)
    return True

def is_authenticated(session):
    return session.get("user") is not None

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not is_authenticated(session):
            return abort(401)
        return f(*args, **kwargs)
    return decorated_function
        