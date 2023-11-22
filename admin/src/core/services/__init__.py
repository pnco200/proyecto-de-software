from src.core.database import db
from src.core.services.service import Service, TipoDeServicio
from src.core.model.model import Institution

from src.core.configuration import get_rows_per_page
from src.core.service_requests import ServiceRequest, ServiceRequestMessages
from sqlalchemy import or_, func, text
from sqlalchemy.orm import joinedload

def list_service_paged(page):
    """ Retorna una lista de servicios paginada

    Args:
        page (_int_): Número de página
    
    Returns:
        Pagination: Lista de servicios paginada
    """
    per_page = get_rows_per_page()
    return Service.query.paginate(page=page, per_page=per_page, error_out=False)

def list_services_paged_by_institution(page, institution_id):
    """ Retorna una lista de servicios paginada por institución

    Args:
        page (_int_): Número de página
        institution_id (_int_): ID de la institución
    
    Returns:
        Pagination: Lista de servicios paginada por institución
    """
    per_page = get_rows_per_page()
    return Service.query.filter_by(institution_id=institution_id).paginate(page=page, per_page=per_page, error_out=False)

def get_service(service_id):
    """Retorna un servicio por ID

    Args:
        service_id (_int_): ID del servicio
    
    Returns:
        Service: Servicio
    """
    return Service.query.get(service_id)

def create_service(**kwargs):
    """Crea un servicio
    
    Args:
        **kwargs: Atributos del servicio

    Returns:
        Service: Servicio creado
    """
    service = Service(**kwargs)
    db.session.add(service)
    db.session.commit()
    return service

def delete_service(service_id):
    """Elimina un servicio

    Args:
        service_id (_int_): id del servicio a eliminar

    Returns:
        _type_: _description_
    """
    try:
        service = Service.query.get(service_id)

        if service:
            service_requests = ServiceRequest.query.filter_by(service_id=service.id).all()
            for service_request in service_requests:
                messages = ServiceRequestMessages.query.filter_by(service_request_id=service_request.id).all()
                for message in messages:
                    db.session.delete(message)
                db.session.delete(service_request)

            db.session.delete(service)
            db.session.commit()
            return True
        else:
            return False 
    except Exception as e:
        print(e)
        return False
    
def update_service(service_id, **kwargs):
    """ Actualiza un servicio

    Args:
        service_id (_int_): ID del servicio
        **kwargs: Atributos a actualizar

    Returns:
        Service: Servicio actualizado
    """
    service = Service.query.get(service_id)
    for key, value in kwargs.items():
        setattr(service, key, value)
    db.session.commit()
    return service

def get_service_types():
    """Retorna los tipos de servicio

    Returns:
        dict: Tipos de servicio
    """
    _dict = {}
    for item in TipoDeServicio:
        _dict[item.name] = item.value
    return _dict

def get_service_by_keyword_and_type(keyword, service_type=None, per_page=None, page=None):
    """Retorna una lista de servicios por palabra clave y tipo de servicio

    Args:
        keyword (_str_): Palabra clave
        service_type (_str_, optional): Tipo de servicio
        per_page (_int_, optional): Cantidad de registros por página
        page (_int_, optional): Número de página

    Returns:
        list: Lista de servicios, int: Cantidad de registros
    """
    query = Service.query

    try:
        query = query.filter(func.array_to_string(Service.key_words, ', ').ilike(f'%{keyword}%'))
        if service_type is not None:
            query = query.filter(Service.type == service_type)
        query = query.join(Institution).options(joinedload(Service.institution))

        total_count = query.count()

        query = query.paginate(page=page, per_page=per_page, error_out=False)
    except Exception as e:
        print(e)
        return False

    return query.items, total_count  



