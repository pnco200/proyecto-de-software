from flask import render_template

def not_found_error404(e):
    kwargs = {
        "error_name":"404 Not Found Error",
        "error_description":"The url does not exist"
    }
    return render_template('error.html',**kwargs), 404