#!/usr/bin/python3
from fabric.api import task
@task
def do_this():
    local('return True')

if __name__ == "__main__":
    check = do_this()
    if check:
        print("all is well!")

