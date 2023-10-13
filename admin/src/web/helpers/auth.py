from functools import wraps
from flask import session, abort
from src.core import auth
def is_authenticated(session):
    return session.get("user") is not None

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not is_authenticated(session):
            return abort(401)
        return f(*args, **kwargs)
    return decorated_function

def has_permission(list_permissions):
   def decorator(f):
       
        @wraps(f)
        def decorated_function(*args, **kwargs):
                
                user = auth.find_user_by_email(session.get("user"))         
                user_permission_list = auth.list_permissions_by_user_id(user.id)
                
                for permission in list_permissions:
                    if not(permission in user_permission_list):
                        print("has_permission === no está el permiso %s" %permission )
                        return abort(401) 
                return f(*args, **kwargs)   
            
        return decorated_function
   return decorator
        