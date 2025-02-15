#!/usr/bin/python3
"""
fabric script to deploy packed web_static archive
"""
from fabric.api import put, run, env
from pathlib import Path

env.hosts = ['100.24.237.103', '54.175.189.210']
env.user = "ubuntu"


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
