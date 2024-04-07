#!/usr/bin/python3
"""Generates a .tgz archive."""
from fabric.api import local
from datetime import datetime


def do_pack():
    """generates archive"""
    file_date = datetime.now().strftime('%Y%m%d%H%M%S')
    file_name = f'web_static_{fdate}.tgz'
    try:
        local('mkdir -p versions')
        local(f'tar -cvzf versions/{file_name} web_static')
    except Exception:
        return None
    return f'versions/{file_name}'
