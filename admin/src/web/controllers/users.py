from flask import Blueprint, render_template, request, redirect, url_for, flash
from src.web.helpers.auth import login_required
from src.core import auth
user_bp = Blueprint('user', __name__, url_prefix='/users')

@user_bp.get('/admin')
#@login_required
def admin_home():
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

@user_bp.get('/')
#@login_required
def home():
    """"Muestra un listado de los usuarios si el usuario esta logeado"""
    page = request.args.get('page', type=int, default=1)
    email = request.args.get('email',type=str,default='')
    users = auth.list_users_paged(page,None,email)
    return render_template("users/home.html", users=users, page=page, email=email)

@user_bp.route('/update_user_status/<int:user_id>') ## TO DO--> Proteger para superADMIN
def update_user_status(user_id):
    user = auth.change_user_status(user_id=user_id)
    if not user:
        flash("No se puede cambiar el estado de ese usuario", "error")
    return redirect(url_for('user.admin_home'))

@user_bp.post('/create_institution_owner') ## TO DO--> Proteger para superADMIN
def create_institution_owner():
    institution_id = request.form.get('institution_id')
    user_id = request.form.get('user_id')

    user = auth.assign_institution_owner(user_id, institution_id)
    if not user:
        flash("No se pudo asignar el usuario como dueño de la institucion", "error")
    return redirect(url_for('user.admin_home'))

#@ValidateQueSeaDueñoDeInstitucion
@user_bp.post('/create_institution_member') ## TO DO--> Proteger para Dueño!, el INSTITUTION ID LO SACA DE LA QUE ESTA SELECIONADA EN LA BARRA
def create_institution_member():
    current_selected_institution = request.form.get('current_selected_institution')
    permission_id = request.form.get('permission_id')
    user_id = request.form.get('user_id')

    user = auth.assign_institution_owner(user_id, permission_id)
    if not user:
        flash("No se pudo asignar el usuario como miembro de la institucion", "error")
    return redirect(url_for('user.home'))

#@ValidateQueSeaDueñoDeInstitucion
@user_bp.post('/delete_institution_member') ## TO DO--> Proteger para Dueño!
def delete_institution_member():
    current_selected_institution = request.form.get('current_selected_institution')
    permission_id = request.form.get('permission_id')
    user_id = request.form.get('user_id')

    user = auth.assign_institution_owner(user_id, permission_id)
    if not user:
        flash("No se pudo asignar el usuario como miembro de la institucion", "error")
    return redirect(url_for('user.home'))


@user_bp.post('/delete_institution_owner') ## TO DO--> Proteger para superADMIN
def delete_institution_owner():
    institution_id = request.form.get('institution_id')
    user_id = request.form.get('user_id')
    user = auth.delete_institution_owner(user_id, institution_id)
    if not user:
        flash("No se pudo eliminar el usuario como dueño de la institucion", "error")
    return redirect(url_for('user.admin_home'))
