from src.core.configuration import get_rows_per_page
from src.core.database import db
from src.core.institutions.institution import Institution
from sqlalchemy import or_

def list_institutions():
    return Institution.query.all()

def get_user_institutions(selected_institution=-1):
    """Returns user institutions, if he has a selected institution it should be sorted to appear first on the list

    Args:
        selected_institution (int, optional): If other value than -1 then there is a selected institution. Defaults to -1.

    Returns:
        list(Institution): Return a list of institutions
    """
    _institutions = Institution.query.all() ## hay que ser que sean las del usuario TO DO
    if selected_institution != -1:
        _institutions.sort(key=lambda institution: (institution.id != selected_institution, institution.id))
    return _institutions

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