from src.core.database import db
from src.core.test.test import Test

def list_tests():
    return Test.query.all()

def create_test(**kwargs):
    test = Test(**kwargs)
    db.session.add(test)
    db.session.commit()
    return test