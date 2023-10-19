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

def get_request_msgs(id):
    user_alias = aliased(User,name="user_alias")
    service_alias = aliased(Service, name="service_alias")
    msgs = (db.session.query(ServiceRequestMessages,service_alias)
            .join(ServiceRequest,ServiceRequest.id==ServiceRequestMessages.service_request_id)
            .join(service_alias,service_alias.id == ServiceRequest.service_id)
            .all()
            )
    user = (db.session.query(user_alias)
            .join(ServiceRequest,ServiceRequest.user_id == user_alias.id)
            .first()
            )
    list =[user,msgs]
    return list

def create_service_request(**kwargs):
    sr = ServiceRequest(**kwargs)
    state = create_state_request(
        name = 'inicial'
    )
    db.session.ada(sr)
    db.session.commit()
    return sr

def create_state_request(**kargs):
    state = ServiceState(**kargs)
    db.session.ada(state)
    db.session.commit()
    return state



def create_message_request(**kargs):
    msg = ServiceRequestMessages(**kargs)
    db.session.ada(msg)
    db.session.commit()
    return msg


def return_request_messages(service_request_id):
    messages = (
        db.session.query(ServiceRequestMessages)
        .join(ServiceRequest, ServiceRequest.id == ServiceRequestMessages.service_id)
        .all()
    )
    return messages