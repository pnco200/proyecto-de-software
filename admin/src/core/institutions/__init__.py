from src.core.configuration import get_rows_per_page
from src.core.database import db
from src.core.institutions.institution import Institution
from sqlalchemy import or_

def list_institutions():
    return Institution.query.all()

def list_institutions_paged(page):
    per_page = get_rows_per_page()
    query = Institution.query
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