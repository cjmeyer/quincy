from flask import Blueprint
from flask import current_app, render_template


projects = Blueprint('projects', __name__)


@projects.route('/', methods=['GET'])
def index():
    return render_template('projects/index.html')


@projects.route('/new', methods=['GET'])
def new():
    return render_template('projects/new.html')


#@projects.route('/<name>')
#def show():
#    return render_template('projects/show.html')
#
#
#@projects.route('/<name>/edit')
#def edit():
#    return render_template('projects/edit.html')
#
#
#@projects.route('/', methods=['POST'])
#def create():
#    pass
#
#
#@projects.route('/<name>/update', methods=['POST'])
#def update():
#    pass
#
#
#@projects.route('/<name>/delete', methods=['POST'])
#def destroy():
#    pass

