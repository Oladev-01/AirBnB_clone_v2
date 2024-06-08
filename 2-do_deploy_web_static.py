#!/usr/bin/python3
"""
    Distributes an archive to web servers.

    Args:
        archive_path (str): Path to the archive file.

    Returns:
        bool: True if all operations were successful, False otherwise.
"""

from fabric.api import *
import os


env.hosts = ['ubuntu@34.232.72.189', 'ubuntu@54.160.114.58']
env.key_filename = ' ~/.ssh/alx_id_rsa'
env.user = 'ubuntu'


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
