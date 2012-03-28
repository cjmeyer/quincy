#! /usr/bin/env python.py

from flaskext.script import Manager, Server, Shell
from quincy import create_app


app = create_app('development')


def make_context():
    return dict(app=app)


manager = Manager(app)
manager.add_command('runserver', Server(host='0.0.0.0', port='4000'))
manager.add_command('shell', Shell(make_context=make_context))


if __name__ == '__main__':
    manager.run()

