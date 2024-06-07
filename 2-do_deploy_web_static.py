#!/usr/bin/python3
"""
This fabric script uncompresses the archive
and then deploys it to the servers.
"""

from fabric import task, env, run, put
import os

# Define the hosts where the script will be deployed
env.hosts = ['ubuntu@34.232.72.189', 'ubuntu@54.160.114.58']

@task
def do_deploy(archive_path):
    """
    Deploy the archived folder to the server and run necessary remote commands.

    Args:
        archive_path (str): The path to the archive file to be deployed.

    Returns:
        bool: True if deployment succeeded, False otherwise.
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Get the filename of the archive folder
        archive_name = os.path.basename(archive_path)
        # The name of the folder which the compressed file will be stored as in the /tmp folder
        tmp_name = f"/tmp/{archive_name}"
        # Copy the local file to the server
        put(archive_path, tmp_name)

        # Define the name of the remote archive folder
        rem_archive_name = "/data/web_static/releases/{}".format(archive_name.split('.')[0])
        run(f"mkdir -p {rem_archive_name}")
        # Extract the compressed file into /data/web_static/releases/ folder
        run(f"tar -xzf {tmp_name} -C {rem_archive_name}")
        # Delete the archived file from /tmp
        run(f"rm {tmp_name}")
        # Move the extracted files from the web_static folder into the parent folder
        run(f"mv {rem_archive_name}/web_static/* {rem_archive_name}")
        # Delete the extracted web_static folder
        run(f"rm -rf {rem_archive_name}/web_static")
        # Delete the symlink pointing to the previous version and create a new one
        run(f"rm /data/web_static/current")
        run(f"ln -s {rem_archive_name} /data/web_static/current")

        return True

    except Exception as e:
        print(f"This is the error: {e}")
        return False

@task
def deploy():
    """
    Execute deployment on all servers.

    This function executes the deployment process by calling the do_deploy
    function for each host specified in env.hosts.

    Returns:
        None
    """
    archive_path = "~/AirBnB_clone_v2/versions/web_static_20240606222430.tgz"
    results = []
    # Call do_deploy for each host
    for host in env.hosts:
        result = do_deploy(archive_path)
        results.append(result)

    if all(results):
        print("New version deployed!")
    else:
        print("Deployment failed on one or more servers.")
