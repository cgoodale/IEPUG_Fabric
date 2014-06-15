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

def local_fabric():
    local("mkdir /tmp/fabric")
    local("cd /tmp/fabric && git clone https://github.com/cgoodale/IEPUG_Fabric.git")
    local("cd /tmp/fabric/IEPUG_Fabric && ls -alhtr")
