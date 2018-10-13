# -*- encoding:utf-8 -*-

import json

def configuration():
    with open("configure.dat", "r") as f:
        data = f.read()
    config = json.loads(data)
    return config

print configuration()