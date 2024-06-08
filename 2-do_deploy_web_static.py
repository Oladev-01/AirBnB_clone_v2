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


def do_deploy(archive_path):
    """
    Distributes an archive to web servers.

    Args:
        archive_path (str): Path to the archive file.

    Returns:
        bool: True if all operations were successful, False otherwise.
    """

    if not os.path.exists(archive_path):
        return False

    # Upload the archive to /tmp
    put(archive_path, '/tmp/')

    # Get the archive filename without extension
    archive_filename = archive_path.split('/')[-1]
    archive_filename_without_ext = archive_filename.split('.')[0]
    rem_archive_name = "/data/web_static/releases/{}".format(
        archive_filename_without_ext)

    # Uncompress the archive
    run(
        f'tar -xzf /tmp/{archive_filename} -C {rem_archive_name}'
    )

    # Delete the archive from the server
    run(f'rm /tmp/{archive_filename}')

    # Moving the extracted files from the web_static
    #  folder into the parent folder
    run(f"mv {rem_archive_name}/web_static/* {rem_archive_name}")
    # Deleting the extracted web_static folder
    run(f"rm -rf {rem_archive_name}/web_static")

    # Delete the symbolic link /data/web_static/current
    run(f'rm  /data/web_static/current')

    # Create a new symbolic link to the new release
    run(
        f"ln -s {rem_archive_name} /data/web_static/current"
    )

    return True
