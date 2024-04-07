#!/usr/bin/python3
"""Deploy archive!"""

from fabric.api import *
import os
from fabric.contrib.files import exists

env.user = 'ubuntu'
env.hosts = ['54.197.110.17', '54.237.32.90']
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers
    """
    if not exists(archive_path):
        return False

    try:
        filename = archive_path.split('/')[-1]
        no_ext = filename.split('.')[0]
        release_path = f'/data/web_static/releases/{no_ext}/'
        tmp_path = '/tmp/' + filename

        put(archive_path, tmp_path)
        run(f'mkdir -p {release_path}')
        run(f'tar -xzf {tmp_path} -C {release_path}')
        run(f'rm {tmp_path}')
        run(f'mv {release_path}web_static/* {release_path}')
        run(f'rm -rf {release_path}web_static')
        run(f'rm -rf /data/web_static/current')
        run(f'ln -s {release_path} /data/web_static/current')

        print("New version deployed!")
        return True
    except:
        return False
