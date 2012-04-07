import signal
import sys

from daemon import Daemon
from path import path
from subprocess import Popen

class MongoDaemon(Daemon):
    def __init__(self, *args, **kw):
        self.dbpath = kw.pop('dbpath', None)
        Daemon.__init__(self, *args, **kw)
    
    def run(self):
        datapath = self.dbpath / 'data'
        if not datapath.isdir():
            datapath.mkdir_p()

        def sigterm(signum, frame):
            self.proc.terminate()
            sys.exit()

        signal.signal(signal.SIGTERM, sigterm)

        cmd = ['mongod']

        cmd.append('--dbpath={0}'.format(datapath.relpath()))
        cmd.append('--logpath={0}'.format(self.dbpath.relpath() / 'log'))

        self.proc = Popen(cmd, cwd=path.getcwd())
        self.proc.communicate()

