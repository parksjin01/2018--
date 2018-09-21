# -*- encoding:utf-8 -*-

def configuration():
    with open("../configure.dat", "r") as f:
        data = f.read().split()
    config = {}
    for item in data:
        config[item.split("=")[0]] = item.split("=")[1]
    return config

print configuration()