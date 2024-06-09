#!/usr/bin/python3
"""
This fabric script:
** imports 1-pack_web_static.py which compresses the
web_static files into a custom file
** imports 2-do_deploy_web_static.py which copies the archived file to
specified remote hosts, uncompresses the file, and makes sure the file is
served on a specified URL by creating a symlink to the file which is already
configured in the Nginx file to serve to that location
"""

from fabric.api import *
import os
do_pack = __import__("1-pack_web_static").do_pack
do_deploy = __import__("2-do_deploy_web_static").do_deploy

env.hosts = ['34.232.72.189', '54.160.114.58']

archive_path = do_pack()


def deploy():
    """
    This function compresses the web_static folder
    and deploys to given hosts
    """
    if not archive_path:
        return False
    return do_deploy(archive_path)

# Example of how to run this script:
# fab -f 3-deploy.py deploy -i ~/.ssh/alx_id_rsa -u ubuntu
