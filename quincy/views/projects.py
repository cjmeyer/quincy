from flask import Blueprint
from flask import current_app


projects = Blueprint('projects', __name__)


@projects.route('/')
def index():
    print current_app.db
    return 'Projects - Index'

