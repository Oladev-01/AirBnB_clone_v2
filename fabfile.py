from fabric.utils import abort
from fabric import task

@task
def commit(c):
    c.run('echo "hey"')

@task
def push(c):
    c.run('ls')