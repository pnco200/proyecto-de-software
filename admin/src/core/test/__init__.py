from src.core.database import db
from src.core.test.test import Test

def list_tests():
    """Metodo que devuelve todas las tuplas test de la base de datos"""
    return Test.query.all()

def create_test(**kwargs):
    """Metodo para crear un test en la base de datos"""
    test = Test(**kwargs)
    db.session.add(test)
    db.session.commit()
    return test