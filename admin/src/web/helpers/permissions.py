from functools import wraps
from flask import session, abort
from src.core import rol_permission as actions
from src.core import auth

def has_permission(list_permissions):
   def decorator(f):
       
        @wraps(f)
        def decorated_function(*args, **kwargs):
                
                user = auth.find_user_by_email(session.get("user"))         
                user_permission_list = actions.list_permissions_by_user_id(user.id)
                
                for permission in list_permissions:
                    if not(permission in user_permission_list):
                        print("has_permission === no está el permiso %s" %permission )
                        return abort(401) 
                return f(*args, **kwargs)   
            
        return decorated_function
   return decorator


def has_permission_In_this_Institution(list_permissions,institution_id):
   def decorator(f):
       
        @wraps(f)
        def decorated_function(*args, **kwargs):
                
                user = auth.find_user_by_email(session.get("user"))     
                institution = 2 ###Aca deberia devolver Id de instituto segun nombre ---> get_id_institution_by_name()     
                user_permission_list = actions.list_permissions_by_user_id(user.id,institution_id)
                
                for permission in list_permissions:
                    if not(permission in user_permission_list):
                        print("has_permission === no está el permiso de la institucion %s" %permission )
                        return abort(401) 
                return f(*args, **kwargs)   
            
        return decorated_function
   return decorator