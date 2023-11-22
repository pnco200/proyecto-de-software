from flask import session
from src.core.database import db
from src.core import services
from src.core import auth 
from src.core.model.model import User,Institution
from src.core.services import Service
from src.core.service_requests.service_request import ServiceRequest, ServiceRequestMessages,ServiceState
from sqlalchemy.orm import joinedload, aliased
from src.core.configuration import get_rows_per_page

def list_requests_paged_by_institution(page, institution_id):
    per_page = get_rows_per_page()
    service_alias = aliased(Service, name="service_alias")
    user_alias = aliased(User, name="user_alias")
    request = (db.session.query(ServiceRequest,service_alias,user_alias)
            .join(service_alias,service_alias.id == ServiceRequest.service_id)
            .join(user_alias, user_alias.id ==ServiceRequest.user_id)
            .filter(service_alias.institution_id == institution_id)
            .paginate(page=page, per_page=per_page, error_out=False)
    )
    ##dejo por si acaso

    return request
def set_new_state(state,request_id):
    request_actual = ServiceRequest.query.filter_by(id=request_id).first()
    request_actual.state_id = state.id
    db.session.commit()
    pass
    
def get_state_by_id(state_id):
    state = aliased(ServiceState,name="state_request")
    s = (db.session.query(state, ServiceRequest)
         .join(ServiceRequest,ServiceRequest.state_id==state.id)
         .first()
         )
    return s
def list_requests_paged_by_user(page, per_page, user_id):
    service_alias = aliased(Service, name="service_alias")
    service_state_alias = aliased(ServiceState, name="service_state_alias")
    user_alias = aliased(User, name="user_alias")
    request = (db.session.query(ServiceRequest,service_alias,user_alias,service_state_alias)
            .join(service_alias,service_alias.id == ServiceRequest.service_id)
            .join(user_alias, user_alias.id == ServiceRequest.user_id)
            .join(service_state_alias, service_state_alias.id == ServiceRequest.state_id)
            .filter(ServiceRequest.user_id == user_id)
            .paginate(page=page, per_page=per_page, error_out=False)
    )
    return request

def list_all_requests_by_user(user_id):
    service_alias = aliased(Service, name="service_alias")
    service_state_alias = aliased(ServiceState, name="service_state_alias")
    user_alias = aliased(User, name="user_alias")
    request = (db.session.query(ServiceRequest,service_alias,user_alias,service_alias)
            .join(service_alias,service_alias.id == ServiceRequest.service_id)
            .join(user_alias, user_alias.id ==ServiceRequest.user_id)
            .join(service_state_alias, service_state_alias.id == ServiceRequest.state_id)
            .filter(ServiceRequest.user_id == user_id)
            .all()
    )
    return request
def get_request_detaile(id):
    service_alias = aliased(Service, name="service_alias")
    user_alias = aliased(User, name="user_alias")
    request = (db.session.query(ServiceRequest,service_alias,user_alias,Institution.name)
            .join(service_alias,service_alias.id == ServiceRequest.service_id)
            .join(user_alias, user_alias.id ==ServiceRequest.user_id)
            .join(Institution, Institution.id == service_alias.institution_id)
            .filter(ServiceRequest.id == id)
            .first()
    )
    return request

def add_message_to_service_request(service_request_id, new_message):
    service_request = ServiceRequest.query.get(service_request_id)

    if service_request:
        if service_request.observations:
            service_request.observations += "\n" + new_message
        else:
            service_request.observations = new_message
        db.session.commit()
        return True
    else:
        return False


def get_request_detaile(id):
    try:
        service_alias = aliased(Service, name="service_alias")
        user_alias = aliased(User, name="user_alias")
        state_of_service = aliased(ServiceState,name="request_state")
        request = (db.session.query(ServiceRequest,service_alias,user_alias,state_of_service)
                .join(service_alias,service_alias.id == ServiceRequest.service_id)
                .join(user_alias, user_alias.id ==ServiceRequest.user_id)
                .join(Institution, Institution.id == service_alias.institution_id)
                .join(state_of_service,state_of_service.id == ServiceRequest.state_id)
                .filter(ServiceRequest.id == id)
                .first()
        )
        return request
    except Exception as e:
        print(e)
        return None

def get_request_msgs(id):
    user_alias = aliased(User,name="user_alias")
    service_alias = aliased(Service, name="service_alias")
    service_request = aliased(ServiceRequest,name="s_request")
    msgs = (db.session.query(ServiceRequestMessages)
            .join(ServiceRequest,ServiceRequest.id==ServiceRequestMessages.service_request_id)
            .join(service_alias,service_alias.id == ServiceRequest.service_id)
            .all()
            )
    s = (db.session.query(service_alias)
         .join(service_request,service_request.service_id==service_alias.id)
         .filter(service_request.id == id)
         .first()
         )
    user = (db.session.query(user_alias)
            .join(ServiceRequest,ServiceRequest.user_id == user_alias.id)
            .first()
            )
    list =[user,msgs,id,s]
    return list

def create_service_request(**kwargs):
    sr = ServiceRequest(**kwargs)
    state = create_state_request(
        name = 'inicial'
    )
    db.session.add(sr)
    db.session.commit()
    return sr

def create_state_request(**kwargs):
    state = ServiceState(**kwargs)
    db.session.add(state)
    db.session.commit()
    return state



def create_message_request(**kwargs):
    try:
        kwargs['user_id']= session.get('user')
        msg = ServiceRequestMessages(**kwargs)
        db.session.add(msg)
        db.session.commit()
        return msg
    except Exception as e:
        print(e)
        return None

def create_user_message(**kwargs):
    msg = ServiceRequestMessages(**kwargs)
    db.session.add(msg)
    db.session.commit()
    return msg


def return_request_messages(service_request_id):
    messages = (
        db.session.query(ServiceRequestMessages)
        .join(ServiceRequest, ServiceRequest.id == ServiceRequestMessages.service_id)
        .all()
    )
    return messages

def filter_service_requests_paged(page, service_type=None, start_date=None, end_date=None, user_name=None, state=None):
    """
    Filtra las solicitudes de servicio según los parámetros proporcionados y las devuelve en forma paginada.

    Args:
        page (int): Número de página.
        service_type (str, optional): Tipo de servicio (correspondiente a los valores de TipoDeServicio).
        start_date (datetime, optional): Fecha inicial del rango para filtrar solicitudes.
        end_date (datetime, optional): Fecha final del rango para filtrar solicitudes.
        user_name (str, optional): Nombre del usuario que realizó la solicitud.
        state (str, optional): Estado de la solicitud.

    Returns:
        Pagination: Objeto paginado con la lista de solicitudes de servicio que coinciden con los criterios de filtrado.
    """
    per_page = get_rows_per_page()
    query = ServiceRequest.query

    if service_type:
        service = Service.query.filter_by(type=service_type).first()
        if service:
            query = query.filter_by(service_id=service.id)

    if start_date and end_date:
        query = query.filter(ServiceRequest.inserted_at.between(start_date, end_date))

    if user_name:
        user = User.query.filter_by(name=user_name).first()
        if user:
            query = query.filter_by(user_id=user.id)

    if state:
        state_entry = ServiceState.query.filter_by(state=state).first()
        if state_entry:
            query = query.filter_by(state_id=state_entry.id)

    return query.paginate(page=page, per_page=per_page, error_out=False)

def get_total_requests_by_institutions():
    """
    Devuelve la cantidad total de solicitudes de servicio por institución.

    Returns:
        list: Lista de tuplas con el nombre de la institución y la cantidad de solicitudes de servicio.
    """
    return (
        db.session.query(Institution.name, db.func.count(ServiceRequest.id))
        .outerjoin(Service, Service.institution_id == Institution.id)
        .outerjoin(ServiceRequest, ServiceRequest.service_id == Service.id)
        .group_by(Institution.name)
        .all()
    )
    return query.all()
