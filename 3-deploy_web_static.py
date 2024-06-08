#!/usr/bin/python3
"""
this fabric script:
** imports 1-pack_web_static.py which compresses the
web_static files into a custom file
** imports 2-do_deploy_web_static.py which copies the archived file to
specified remote hosts, uncompresses the file and make sure the file is
served on a specified url by creating a symlink to the file which is already
configured in the Nginx file to serve to that location
"""

from fabric.api import *
import os
do_pack = __import__("1-pack_web_static").do_pack
do_deploy = __import__("2-do_deploy_web_static").do_deploy


def deploy():
    """
    this function compresses the web_static folder
    and deploys to given hosts
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
