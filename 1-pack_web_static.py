#!/usr/bin/env bash
# generates a .tgz archive
from fabric.api import local
from datetime import datetime


def do_pack():
    """ generates archive"""
    try:
        file_date = datetime.now().strftime('%Y%m%d%H%M%S')
        file_name = "web_static_" + file_date
        archive = 'versions/{}.tgz'.format(file_name)

        local('mkdir -p versions')
        local('tar -czvf {} web_static'.format(archive))
        return archive
    except Exception:
        return None
