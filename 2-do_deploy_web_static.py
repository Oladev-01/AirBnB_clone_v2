#!/usr/bin/python3
"""
This fabric script uncompress the archive
and then deploy to the servers
"""

from fabric.connection import Connection
from fabric import task
import os


env_hosts = ['ubuntu@34.232.72.189', 'ubuntu@54.160.114.58']


@task
def do_deploy(c, archive_path):
    """this function deploys the archived folder to the server
    and running necessary remote commands on the server"""

    if not os.path.exists(archive_path):
        return False

# try and exception to catch error if there is
    try:
        # getting the filename of the archive folder
        archive_name = os.path.basename(archive_path)
        # the name of the folder which the compressed file will
        #  be stored as in the /tmp folder
        tmp_name = f"/tmp/{archive_name}"
        # like scp, copying the local file to the server
        c.put(archive_name, tmp_name)

        rem_archive_name = "/data/web_static/releases/{}".format(
            archive_name.split('.')[0])
        c.run(f"mkdir -p {rem_archive_name}")
        # extracting the compressed file into /data/web_static/releases/ folder
        c.run(f"tar -xzf {tmp_name} -C {rem_archive_name}")
        # deleting the archived file from /tmp
        c.run(f"rm {tmp_name}")
        # moving the extracted files from the web_static
        #  folder into the parent folder
        c.run(f"mv {rem_archive_name}/web_static/* {rem_archive_name}")
        # deleting the extracted web_static folder
        c.run(f"rm -rf {rem_archive_name}/web_static")
        # deleting the sym link which was pointing
        #  to /data/web_static/releases/test
        # and make it point to the uncompressed folder
        c.run(f"rm /data/web_static/current")
        c.run(f"ln -s {rem_archive_name} /data/web_static/current")

        return True

    except Exception as e:
        print(f"this is the error: {e}")


def deploy():
    """this function executes deployment on all servers"""

    archive_path = "~/AirBnB_clone_v2/versions/web_static_20240606222430.tgz"
    results = []
    # opening connection to the hosts
    for host in env_hosts:
        with Connection(host) as c:
            result = do_deploy(c, archive_path)
            results.append(result)

    if all(results):
        print("New version deployed!")
