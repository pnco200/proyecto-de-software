from src.core.configuration import get_rows_per_page
from src.core.database import db
from src.core.institutions.institution import Institution
from sqlalchemy import or_

def list_institutions():
    return Institution.query.all()

def list_institutions_paged(page):
    per_page = get_rows_per_page()
    query = Institution.query.order_by(Institution.id.asc())
    return query.paginate(page=page, per_page=per_page, error_out=False)

def create_institution(**kwargs):
    try:
        institution = Institution(**kwargs)
        db.session.add(institution)
        db.session.commit()
        return institution
    except Exception as e:
        print(e)
        return None

def institution_exists(name):
    return Institution.query.filter_by(name=name).first() is not None

def get_institution_by_id(id):
    return Institution.query.filter_by(id=id).first()

def update_institution(id, **kwargs):
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