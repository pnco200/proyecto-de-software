from flask import Blueprint, render_template, request, redirect, url_for, flash
from src.core import service_requests
from src.web.helpers.utils import current_selected_institution
from src.web.helpers import permissions
srequest_bp = Blueprint('servicesRequests', __name__, url_prefix='/srequests')

@srequest_bp.get('/')
@permissions.permission_required_in_Institution(["request_index"])
def list_service_request():
    page = request.args.get('page', type=int, default=1)
    list = service_requests.list_requests_paged_by_institution(page, current_selected_institution())    
    return render_template("services_requests/index.html", request=list, page=page)


@srequest_bp.get('/request_detaile/<int:request_id>')
@permissions.permission_required_in_Institution(["request_show"])
def see_request_detaile(request_id):
    """
       Presentara el detaller de una solicitud
    """
    r = service_requests.get_request_detaile(request_id)
    return render_template("services_requests/request_detaile.html", request=r)

@srequest_bp.get('/request_msgs/<int:request_id>')
@permissions.permission_required_in_Institution(["request_show"])
def see_request_msgs(request_id):
        """
        Mostrara los mensajes relacionados con una solicitud
        """
        user_and_msgs = service_requests.get_request_msgs(request_id)
    
        user_and_msgs[1] = sorted(user_and_msgs[1], key=lambda msg: msg.inserted_at)
        return render_template("services_requests/request_msgs.html",user_and_msgs = user_and_msgs)



@srequest_bp.post('/send_request_msg')
@permissions.permission_required_in_Institution(["request_update"])
def send_msg():
    """
        Estos permitiran que se envie un mensaje al cliente en la solicitud
    """
    nuevo_mensaje = request.form.get('nuevo_mensaje')
    service_request = request.form.get('service_request')
    
    if not nuevo_mensaje.strip():  # Verifica si el mensaje es vacío o contiene solo espacios en blanco
        flash("No se puede enviar un mensaje vacío", "error")
        return redirect(url_for('servicesRequests.see_request_msgs', request_id=service_request))

    msg = service_requests.create_message_request(
        service_request_id=service_request,
        msg_content=nuevo_mensaje,
        user_id=0
    )
    return redirect(url_for('servicesRequests.see_request_msgs', request_id=service_request))
@srequest_bp.get('/see_state_request/<int:request_id>/<int:state_id>')
@permissions.permission_required_in_Institution(["request_show"])
def see_state_request(request_id,state_id):
    """
       Mostrara el estado de la solicitud y se podra cambiar
    """
    state = service_requests.get_state_by_id(state_id)  
    return render_template('services_requests/state.html', state = state,request_id = request_id)

@srequest_bp.post('/change_state/<int:request_id>')
@permissions.permission_required_in_Institution(["request_update"])
def change_state(request_id):
    """
       cambia el estado con los parametros pasados
    """
    nuevo_mensaje = request.form.get('new_observations')
    estado = request.form.get('new_state')
    new_state = service_requests.create_state_request(
        name = estado,
        state_message = nuevo_mensaje
    )
    new_state_request = service_requests.set_new_state(new_state,request_id)
    return redirect(url_for('servicesRequests.see_state_request', request_id=request_id,state_id=new_state.id))

