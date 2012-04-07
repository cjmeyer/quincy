import sys

from fabric.api import task
from utils.mongod import MongoDaemon
from utils.path import path

@task
def mongo(cmd):
    dbdir = path('/') / 'tmp' / 'quincy-mongodb'
    if not dbdir.isdir():
        dbdir.makedirs_p()

    daemon = MongoDaemon('/tmp/quincy-mongodb.pid', dbpath=dbdir)

    if cmd == 'start':
        daemon.start()
    elif cmd == 'stop':
        daemon.stop()
    elif cmd == 'restart':
        daemon.restart()
    else:
        print 'unknown command'

    sys.exit()

