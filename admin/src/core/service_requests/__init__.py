from flask import session
from src.core.database import db
from src.core import services
from src.core import auth 
from src.core.model.model import User,Institution
from src.core.services import Service
from src.core.service_requests.service_request import ServiceRequest, ServiceRequestMessages,ServiceState
from sqlalchemy.orm import joinedload, aliased
from src.core.configuration import get_rows_per_page
import random
from datetime import datetime, timedelta
def list_requests_paged_by_institution(page, institution_id, service_type=None, start_date=None, end_date=None, service_state=None):
    per_page = get_rows_per_page()
    service_alias = aliased(Service, name="service_alias")
    user_alias = aliased(User, name="user_alias")
    query = (db.session.query(ServiceRequest,service_alias,user_alias)
            .join(service_alias,service_alias.id == ServiceRequest.service_id)
            .join(user_alias, user_alias.id ==ServiceRequest.user_id)
            .filter(service_alias.institution_id == institution_id)
    )
    if service_type:
        query = query.filter(service_alias.type == service_type)
    
    if start_date and end_date:
        query = query.filter(ServiceRequest.inserted_at.between(start_date, end_date))

    if service_state:
         state = ServiceState.query.filter_by(name=service_state).first()
         if state:
             query = query.filter(ServiceRequest.state_id == state.id)
    
    return query.paginate(page=page, per_page=per_page, error_out=False)

def set_new_state(state,request_id):
    request_actual = ServiceRequest.query.filter_by(id=request_id).first()
    request_actual.state_id = state.id
    db.session.commit()
    pass
def get_service_from_request(r_id):
    service = (db.session.query(Service)
        .join(ServiceRequest, ServiceRequest.service_id == Service.id)
        .filter(ServiceRequest.id == r_id)
        .first())

    return service

def get_user_from_request(r_id):
    user = (db.session.query(User)
        .join(ServiceRequest, ServiceRequest.user_id == User.id)
        .filter(ServiceRequest.id == r_id)
        .first())

    return user

def get_state_by_id(state_id):
    state = aliased(ServiceState,name="state_request")
    s = (db.session.query(state, ServiceState)
     .join(ServiceState, ServiceState.id == state.id)
     .filter(ServiceState.id == state_id)
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
    msgs = (db.session.query(ServiceRequestMessages)
        .join(ServiceRequestMessages.service_request)  # Aquí especificamos la relación
        .filter(ServiceRequest.id == id)  # Filtramos por el id de la solicitud de servicio
        .all()
    )
    print(msgs)
    return msgs

def create_service_request(**kwargs):
    # Extraer la información necesaria de kwargs
    service_id = kwargs.get('service_id')
    user_id = kwargs.get('user_id')
    observations = kwargs.get('observations')
    archive = kwargs.get('archive')

    # Leer el contenido binario del archivo
    file_data = archive.read() if archive else None

    # Crear el estado (supongo que es una función que ya tienes definida)
    state = create_state_request(name='inicial')

    # Crear la instancia de ServiceRequest
    sr = ServiceRequest(
        service_id=service_id,
        user_id=user_id,
        observations=observations,
        archive=file_data,
        state_id=state.id
    )

    # Agregar a la sesión y hacer commit
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
def create_message_request_portal(**kwargs):
    msg = ServiceRequestMessages(**kwargs)
    db.session.add(msg)
    db.session.commit()
    return msg
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

def get_top_institutions_less_time_per_request():
    """
    Devuelve las 10 instituciones con el menor tiempo promedio por solicitud de servicio.

    Returns:
        list: Lista de tuplas con el nombre de la institución y el tiempo promedio por solicitud de servicio.
    """
    return (
        db.session.query(Institution.name, db.func.avg(ServiceRequest.updated_at - ServiceRequest.inserted_at))
        .outerjoin(Service, Service.institution_id == Institution.id)
        .outerjoin(ServiceRequest, ServiceRequest.service_id == Service.id)
        .join(ServiceState, ServiceState.id == ServiceRequest.state_id)
        .filter(ServiceState.name == "finalizada")
        .group_by(Institution.name)
        .order_by(db.func.avg(ServiceRequest.updated_at - ServiceRequest.inserted_at).asc())
        .limit(5)
        .all()
    )

def get_most_requested_services():
    """
    Devuelve los 10 servicios más solicitados y su institucion.

    Returns:
        list: Lista de tuplas con el nombre del servicio y la cantidad de solicitudes de servicio.
    """
    return (
        db.session.query(Service.name, Institution.name, db.func.count(ServiceRequest.id))
        .outerjoin(ServiceRequest, ServiceRequest.service_id == Service.id)
        .outerjoin(Institution, Institution.id == Service.institution_id)
        .group_by(Service.name, Institution.name)
        .order_by(db.func.count(ServiceRequest.id).desc())
        .limit(5)
        .all()
    )

def set_new_state_seeds(state, request_id):
    request_actual = ServiceRequest.query.filter_by(id=request_id).first()
    request_actual.state_id = state.id

    random_days = random.randint(0, 50)
    random_timedelta = timedelta(days=random_days)

    request_actual.updated_at = datetime.utcnow() + random_timedelta

    db.session.commit()
