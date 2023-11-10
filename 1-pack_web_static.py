#!/usr/bin/python3
"""
fabric script to pack web_static
"""
from fabric.api import local
from datetime import datetime
from os import path


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
