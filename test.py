#!/usr/bin/python3
try:
    from paramiko import auth_strategy
    print("paramiko.auth_strategy exists")
except ImportError:
    print("paramiko.auth_strategy does not exist")
