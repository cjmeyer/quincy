from flask import Blueprint


projects = Blueprint('projects', __name__)


@projects.route('/')
def index():
    return 'Projects - Index'

