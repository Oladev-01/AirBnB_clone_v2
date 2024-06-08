from fabric.utils import abort
from fabric import task
from fabric.state import env

@task
def commit(c):
    c.run('echo "hey"')

@task
def push(c):
    c.run('ls')