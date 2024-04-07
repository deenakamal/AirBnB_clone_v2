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
    """Function for deploy"""
    if not os.path.exists(archive_path):
        return False

    data_path = '/data/web_static/releases/'
    tmp = archive_path.split('.')[0]
    name = tmp.split('/')[1]
    dest = data_path + name

    try:
        put(archive_path, '/tmp')
        run('sudo mkdir -p {}'.format(dest))
        run('sudo tar -xzf /tmp/{}.tgz -C {}'.format(name, dest))
        run('sudo rm -f /tmp/{}.tgz'.format(name))
        run('sudo mv {}/web_static/* {}/'.format(dest, dest))
        run('sudo rm -rf {}/web_static'.format(dest))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -sf {} /data/web_static/current'.format(dest))
        run('sudo chown -R ubuntu:ubuntu /data/')
        return True
    except:
        return False


def deploy():
    """creates and distributes an archive
    """
    archive_path = do_pack()
    if archive_path:
        return do_deploy(archive_path)
    else:
        return False
