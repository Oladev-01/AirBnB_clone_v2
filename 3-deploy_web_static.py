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
from datetime import datetime
env.hosts = ['ubuntu@34.232.72.189', 'ubuntu@54.160.114.58']
env.user = 'ubuntu'


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


def do_deploy(archive_path):
    """
    Distributes the archive to web servers using Fabric.

    Args:
        archive_path: The path to the archive to be deployed.

    Returns:
        True if all operations have been done correctly, otherwise False.
    """
    # Check if the archive exists
    if not os.path.exists(archive_path):
        return False

    # Extract the filename from the archive path
    filename = os.path.basename(archive_path)
    archive_name = os.path.splitext(filename)[0]

    # Upload the archive to /tmp/ directory of the web servers
    put(archive_path, '/tmp/')

    # Uncompress the archive to /data/web_static/releases
    # /<archive filename without extension>
    run('mkdir -p /data/web_static/releases/{}'.format(archive_name))
    run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.
        format(filename, archive_name))

    # Delete the archive from the web servers
    run('rm /tmp/{}'.format(filename))
    run('mv /data/web_static/releases/{}/web_static/* \
         /data/web_static/releases/{}'.
        format(archive_name, archive_name))
    run('rm -rf /data/web_static/releases/{}/web_static/'.format(archive_name))
    # Delete the symbolic link /data/web_static/current
    run('rm -rf /data/web_static/current')

    # Create a new symbolic link /data/web_s
    # tatic/current linked to the new version
    run('ln -s /data/web_static/releases/{}/ \
        /data/web_static/current'.format(archive_name))

    return True


def deploy():
    """
    this function compresses the web_static folder
    and deploys to given hosts
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
