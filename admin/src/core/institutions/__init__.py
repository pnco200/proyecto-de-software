from src.core.configuration import get_rows_per_page
from src.core.database import db
from src.core.model.model import Institution, RolUsuario
from sqlalchemy import or_

def list_institutions():
    """Devuelve una lista de todas las instituciones

    Returns:
        list: lista de instituciones
    """
    return Institution.query.all()

def get_user_institutions(user_id,selected_institution=-1):
    """Devuelve una lista de instituciones de un usuario

    Args:
        user_id (_int_): El id del usuario
        selected_institution (_int_): El id de la institucion seleccionada
    
    Returns:
        list: lista de instituciones del usuario
    """
    _institutions = (
        db.session.query(Institution)
        .join(RolUsuario, RolUsuario.user_id == user_id)
        .filter(Institution.id == RolUsuario.institution_id)
        .all()
    )
    if selected_institution != -1:
        _institutions.sort(key=lambda institution: (institution.id != selected_institution, institution.id))
    return _institutions

def get_first_institution_id(user_id):
    """Devuelve el id de la primera institucion del usuario

    Args:
        user_id (_int_): El id del usuario
    
    Returns:
        int: id de la primera institucion del usuario
    """
    _institutions = (
        db.session.query(Institution)
        .join(RolUsuario, RolUsuario.user_id == user_id)
        .filter(Institution.id == RolUsuario.institution_id)
        .all()
    )    

    if _institutions:
        return _institutions[0].id
    else:
        return None

def list_institutions_paged(page):
    """Devuelve una lista de instituciones paginada y ordenada por id ascendentemente
   
     Args:
        page (_int_): numero de pagina
    
    Returns:
        list: lista de instituciones
    """
    per_page = get_rows_per_page()
    query = Institution.query.order_by(Institution.id.asc())
    return query.paginate(page=page, per_page=per_page, error_out=False)

def list_institutions_paged_api(page, per_page):
    """Devuelve una lista de instituciones paginada y ordenada por id ascendentemente
   
     Args:
        page (_int_): numero de pagina
    
    Returns:
        list: lista de instituciones
    """
    query = Institution.query.order_by(Institution.id.asc())
    return query.paginate(page=page, per_page=per_page, error_out=False)

def create_institution(**kwargs):
    """Crea una institucion

    Args:
        **kwargs: parametros de la institucion a crear

    Returns:
        Institution: institucion creada
    """
    try:
        institution = Institution(**kwargs)
        db.session.add(institution)
        db.session.commit()
        return institution
    except Exception as e:
        print(e)
        return None

def institution_exists(name):
    """Comprueba si existe una institucion con el nombre pasado por parametro

    Args:
        name (_str_): nombre de la institucion
    Returns:
        bool: True si existe, False en caso contrario
    """
    return Institution.query.filter_by(name=name).first() is not None

def get_institution_by_id(id):
    return Institution.query.filter_by(id=id).first()

def update_institution(id, **kwargs):
    """Actualiza una institucion

    Args:
        id (_int_): id de la institucion
        **kwargs: parametros a actualizar

    Returns:
        Institution: institucion actualizada
    """
    try:
        institution = get_institution_by_id(id)
        if institution is None:
            return None
        for key, value in kwargs.items():
            setattr(institution, key, value)
        db.session.commit()
        return institution
    except Exception as e:
        print(e)
        return None

def delete_institution(id):
    """Elimina una institucion

    Args:
        id (_int_): id de la institucion

    Returns:
        Institution: institucion eliminada
    """
    try:
        institution = get_institution_by_id(id)
        if institution is None:
            return None
        db.session.delete(institution)
        db.session.commit()
        return institution
    except Exception as e:
        print(e)
        return None
