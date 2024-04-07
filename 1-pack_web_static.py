#!/usr/bin/python3
"""Generates a .tgz archive."""
from fabric.api import local
from datetime import datetime


def do_pack():
    """generates archive"""
    file_date = datetime.now().strftime('%Y%m%d%H%M%S')
    file_name = f'web_static_{file_date}.tgz'
    try:
        local('mkdir -p versions')
        local(f'tar -czvf versions/{file_name} web_static')
        return f'versions/{file_name}'
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
