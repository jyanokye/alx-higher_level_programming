#!/usr/bin/python3
"""initializate something"""
import requests


def status():
    """a Python script that fetches https://intranet.hbtn.io/status"""

    req = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))


if __name__ == '__main__':
    status()
