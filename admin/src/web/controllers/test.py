from flask import Blueprint, render_template
from src.core import test

test_bp = Blueprint('test', __name__, url_prefix='/test')

@test_bp.get('/')
def index():
    tests = test.list_tests()
    return render_template('test/index.html', tests=tests)

def create():
    pass

def update():
    pass

def delete():
    pass

