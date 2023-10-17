from functools import wraps
from flask import session, abort, redirect, url_for, flash
from src.core import rol_permission as actions
from src.core import auth
from src.core import institutions
def has_permission(list_permissions):
   def decorator(f):
       
        @wraps(f)
        def decorated_function(*args, **kwargs):                
                user = session.get("user")   
                if not user:
                     flash("Debe estar logeado para acceder a este recurso","info")
                     redirect(url_for("auth.login"))       
                user_permission_list = actions.list_permissions_by_user_id(user.id)
                
                for permission in list_permissions:
                    if not(permission in user_permission_list):
                        print("has_permission === no está el permiso %s" %permission )
                        return abort(401) 
                return f(*args, **kwargs)   
            
        return decorated_function
   return decorator


def permission_required_in_Institution(list_permissions):
   def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
                institution_id = kwargs.get('institution_id', None)
                user = session.get("user")
                if not user:
                     flash("Debe estar logeado para acceder a este recurso","info")
                     redirect(url_for("auth.login")) 
                user_permission_list = actions.list_permissions_by_user_id(user.id,institution_id)
                for permission in list_permissions:
                    if not(permission in user_permission_list):
                        print("No posee el permiso en la institucion para la accion que desea. No posee permiso %s" %permission )
                        return abort(401) 
                return f(*args, **kwargs)   
            
        return decorated_function
   return decorator