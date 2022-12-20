#!/usr/bin/python3
"""initializate something"""
import requests


def status():
    """a Python script that fetches https://intranet.hbtn.io/status"""

    response = requests.get('https://alx-intranet.hbtn.io/status')
    return response


if __name__ == '__main__':
    status = get_status()
    print("Body response:")
    print("\t- type:", type(status.text))
    print("\t- content:", status.text)
