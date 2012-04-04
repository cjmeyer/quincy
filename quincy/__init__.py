import os
from flask import Flask

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('quincy.config.{0}'.format(config_name))
    app.config.from_pyfile('quincy.cfg', silent=True)
    app.config.from_envvar('QUINCY_SETTINGS', silent=True)

    from quincy.views.projects import projects

    app.register_blueprint(projects, url_prefix='/projects')

    return app

