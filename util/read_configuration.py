"""
    Read Configuration
    ~~~~~~~~~~~~~~~~~~
"""

# -*- encoding:utf-8 -*-
import json

def configuration():
    """
    Read configuration from text file

    :return: Configurations
    """
    with open("configure.dat", "r") as f:
        data = f.read()
    config = json.loads(data)
    return config
