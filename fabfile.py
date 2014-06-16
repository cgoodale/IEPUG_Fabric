""" Simple Example fabfile to demonstrate some of Fabric's 
features
"""

import platform


def hostname():
    print platform.node()


def hello(name="Jack"):
    print "Hello, %s!" % (name, )



"""Use the local api now"""

from fabric.api import local

def clone_demo(root_dir='/tmp/fabric'):
    local("mkdir %s" % root_dir)
    local("cd %s && git clone https://github.com/cgoodale/IEPUG_Fabric.git" % root_dir)
    local("cd %s/IEPUG_Fabric && ls -alhtr" % root_dir)

def check_demo(root_dir='/tmp/fabric'):
    local("cd %s/IEPUG_Fabric && wc fabfile.py" % root_dir)
    local("cd %s/IEPUG_Fabric && vi fabfile.py" % root_dir)
    local("cd %s/IEPUG_Fabric && git status" % root_dir)


