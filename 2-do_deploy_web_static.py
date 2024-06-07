#!/usr/bin/python3
"""
This fabric script uncompresses the archive
and then deploys it to the servers
"""

from fabric import task, env, run, put, local
import os

env.hosts = ['ubuntu@34.232.72.189', 'ubuntu@54.160.114.58']


@task
def do_deploy(archive_path):
    """this function deploys the archived folder to the server
    and runs necessary remote commands on the server"""

    if not os.path.exists(archive_path):
        return False

    try:
        # getting the filename of the archive folder
        archive_name = os.path.basename(archive_path)
        # the name of the folder which the compressed file will
        #  be stored as in the /tmp folder
        tmp_name = f"/tmp/{archive_name}"
        # like scp, copying the local file to the server
        put(archive_path, tmp_name)

        rem_archive_name = "/data/web_static/releases/{}".format(
            archive_name.split('.')[0])
        run(f"mkdir -p {rem_archive_name}")
        # extracting the compressed file into /data/web_static/releases/ folder
        run(f"tar -xzf {tmp_name} -C {rem_archive_name}")
        # deleting the archived file from /tmp
        run(f"rm {tmp_name}")
        # moving the extracted files from the web_static
        #  folder into the parent folder
        run(f"mv {rem_archive_name}/web_static/* {rem_archive_name}")
        # deleting the extracted web_static folder
        run(f"rm -rf {rem_archive_name}/web_static")
        # deleting the sym link which was pointing
        #  to /data/web_static/releases/test
        # and make it point to the uncompressed folder
        run(f"rm /data/web_static/current")
        run(f"ln -s {rem_archive_name} /data/web_static/current")

        return True

    except Exception as e:
        print(f"this is the error: {e}")
        return False


@task
def deploy():
    """this function executes deployment on all servers"""

    archive_path = "~/AirBnB_clone_v2/versions/web_static_20240606222430.tgz"
    results = []
    # opening connection to the hosts
    for host in env.hosts:
        result = do_deploy(archive_path)
        results.append(result)

    if all(results):
        print("New version deployed!")
    else:
        print("Deployment failed on one or more servers.")
