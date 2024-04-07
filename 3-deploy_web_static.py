#!/usr/bin/python3
"""Generates a .tgz archive."""
from fabric.api import local, env, put, run
from datetime import datetime
from fabric.contrib import files
import os

env.user = "ubuntu"
env.hosts = ["54.197.110.17", "54.237.32.90"]


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


def do_deploy(archive_path):
    """do_deploy"""
    if not os.path.exists(archive_path):
        return False

    _path = '/data/web_static/releases/'
    name = archive_path.split('/')[-1].split('.')[0]
    last = _path + name
    try:
        put(archive_path, '/tmp')
        run('sudo mkdir -p {}'.format(dest))
        run('sudo tar -xzf /tmp/{}.tgz -C {}'.format(name, last))
        run('sudo rm -f /tmp/{}.tgz'.format(name))
        run('sudo mv {}/web_static/* {}/'.format(last, last))
        run('sudo rm -rf {}/web_static'.format(last))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -sf {} /data/web_static/current'.format(last))
        run('sudo chown -R ubuntu:ubuntu /data/')
        return True
    except:
        return False


def deploy():
    """
    deploy
    """
    _path = do_pack()
    if _path:
        return do_deploy(_path)
    else:
        return False
