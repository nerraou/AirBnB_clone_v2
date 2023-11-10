#!/usr/bin/python3
"""
fabric script to pack and deploy web_static
"""

from fabric.api import local, run, put, env
from datetime import datetime
from os import path
from pathlib import Path


env.hosts = ['100.24.237.103', '54.175.189.210']


def do_pack():
    """
    create web_static archive
    """
    formated_date = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "versions/web_static_{}.tgz".format(formated_date)
    local("mkdir -p versions")
    result = local("tar -czvf {} ./web_static/".format(archive_name))

    if result.succeeded:
        size = path.getsize(archive_name)
        print("web_static packed: {} -> {}Bytes".format(archive_name, size))
        return archive_name
    return None


def do_deploy(archive_path):
    """
    deploy web_static archive
    """

    basename = Path(archive_path).stem
    release_path = "/data/web_static/releases/{}".format(basename)

    try:
        put(archive_path, "/tmp")
        run("mkdir -p {}".format(release_path))
        run("tar -xzf /tmp/{}.tgz -C {}".format(basename, release_path))
        run("mv {}/web_static/* {}/".format(release_path, release_path))
        run("rm -f /tmp/{}".format(archive_path))
        run("rm -f /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(release_path))

        return True
    except Exception:
        return False


def deploy():
    """
    deploy web_static
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
