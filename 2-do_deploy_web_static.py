#!/usr/bin/python3
"""Distrubute archive"""

from fabric.api import *
import os
from fabric.contrib import files

env.user = 'ubuntu'
env.hosts = ['54.197.110.17', '54.237.32.90']


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
    except Exception:
        return False
