""" Simple Example fabfile to demonstrate some of Fabric's 
features
"""

import platform


def hostname():
    print platform.node()
