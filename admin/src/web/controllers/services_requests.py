from flask import Blueprint, render_template, request, redirect, url_for, flash
from src.core import service_requests
from src.web.helpers.utils import current_selected_institution
from src.web.helpers import permissions
srequest_bp = Blueprint('servicesRequests', __name__, url_prefix='/srequests')

@srequest_bp.get('/')
##@permissions.permission_required_in_Institution(["institution_show"], request)
def list_service_request():
    page = request.args.get('page', type=int, default=1)
    list = service_requests.list_requests_paged_by_institution(page, current_selected_institution())    
    return render_template("services_requests/index.html", request=list, page=page)


@srequest_bp.get('/request_detaile/<int:request_id>')
def see_request_detaile(request_id):
    r = service_requests.get_request_detaile(request_id)
    return render_template("services_requests/request_detaile.html", request=r)

@srequest_bp.get('/request_msgs/<int:request_id>')
def see_request_msgs(request_id):
    user_and_msgs = service_requests.get_request_msgs(request_id)
    if not user_and_msgs[1]:
        flash("No hay mensajes en la solicitud")
        return  redirect(url_for('servicesRequests.list_service_request'))
    else:
        user_and_msgs[1] = sorted(user_and_msgs[1], key=lambda msg: msg.ServiceRequestMessages.inserted_at)
        return render_template("services_requests/request_msgs.html",user_and_msgs = user_and_msgs)
