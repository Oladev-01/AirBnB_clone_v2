from fabric import task

@task
def my_task(c):
    c.local('echo "hello world"')