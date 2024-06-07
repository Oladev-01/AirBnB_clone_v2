#!/usr/bin/python3
"""this module defines a fabric file that compresses the web_static folder"""
from fabric.api import *
import os
from datetime import datetime


def do_pack():
    """this function creates a .tgz archive file of web_static folder"""

    # checks if the folder /version exists
    if not os.path.exists("versions"):
        os.mkdir("versions")
    time_of_crt = datetime.now()
    archive_name = "web_static_{}.tgz".format(time_of_crt.
                                              strftime("%Y%m%d%H%M%S"))
    local("tar -cvzf versions/{} web_static".format(archive_name))

    archive_path = "versions/{}".format(archive_name)
    if os.path.exists(archive_path):
        return archive_path
    else:
        return None
