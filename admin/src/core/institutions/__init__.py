from src.core.database import db
from admin.src.core.institutions.institution import Institution
from sqlalchemy import or_

def list_institutions():
    return Institution.query.all()
    
def create_institution(**kwargs):
    institution = Institution(**kwargs)
    db.session.add(institution)
    db.session.commit()
    return institution

