#!/usr/bin/python3
""" do_clean """

from fabric.api import local, run, env
import os

env.user = 'ubuntu'
env.hosts = ['54.197.110.17', '54.237.32.90']


def do_clean(number=0):
    """ do_clean"""
    if int(number) == 0:
        number = 1
    number = int(number) + 1
    local("ls -dt versions/* | tail -n +{} | sudo xargs rm -fr".format(number))
    path = "/data/web_static/releases/*"
    run("ls -dt {} | tail -n +{} | sudo xargs rm -fr".format(path, number))
