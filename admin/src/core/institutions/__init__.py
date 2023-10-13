from src.core.database import db
from src.core.institutions.institution import Institution
from sqlalchemy import or_

def list_institutions():
    return Institution.query.all()
    
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