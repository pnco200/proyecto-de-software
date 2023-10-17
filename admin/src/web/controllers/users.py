from flask import Blueprint, render_template, request, redirect, url_for, flash
from src.web.helpers.auth import login_required
from src.core import auth
from src.web.helpers.permissions import has_permission,permission_required_in_Institution
user_bp = Blueprint('user', __name__, url_prefix='/users')

@user_bp.get('/index')

@has_permission(["user_index"])
def home():
    """"Muestra un listado de los usuarios si el usuario esta logeado"""
    page = request.args.get('page', type=int, default=1)
    only_blocked = request.args.get('blocked',default=None)
    email = request.args.get('email',type=str,default='')
    if only_blocked == "False":
        only_blocked = False
    elif only_blocked == "True":
        only_blocked = True
    else:
        only_blocked = None
    users = auth.list_users_paged(page,only_blocked,email)
    return render_template("users/index.html", users=users, page=page, blocked=only_blocked, email=email)

@user_bp.route('/update_user_status/<int:user_id>') ## TO DO--> Proteger para superADMIN
@has_permission(["user_update"])##--> ver cuales necesita
def update_user_status(user_id):
    user = auth.change_user_status(user_id=user_id)
    if not user:
        flash("No se puede cambiar el estado de ese usuario", "error")
    return redirect(url_for('user.home'))

@user_bp.post('/create_institution_owner') ## TO DO--> Proteger para superADMIN
@has_permission([""])##--> ver cuales necesita
def create_institution_owner():
    institution_id = request.args.get('institution_id',type=int,default=None)
    user_id = request.args.get('user_id',type=int,default=None)

    user = auth.assign_institution_owner(user_id, institution_id)
    if not user:
        flash("No se pudo asignar el usuario como dueño de la institucion", "error")
    return redirect(url_for('user.home'))

@user_bp.post('/delete_institution_owner') ## TO DO--> Proteger para superADMIN

def delete_institution_owner():
    institution_id = request.args.get('institution_id',type=int,default=None)
    user_id = request.args.get('user_id',type=int,default=None)
    user = auth.delete_institution_owner(user_id, institution_id)
    if not user:
        flash("No se pudo eliminar el usuario como dueño de la institucion", "error")
    return redirect(url_for('user.home'))
