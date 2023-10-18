from flask import render_template

def not_found_error404(e):
    kwargs = {
        "error_name":"404 Not Found Error",
        "error_description":"The url does not exist"
    }
    return render_template('error.html',**kwargs), 404

def unauthorized(e):
    kwargs = {
        "error_name":"401 Unauthorized",
        "error_description":"No tiene acceso a este recurso."
    }
    return render_template('error.html',**kwargs), 401