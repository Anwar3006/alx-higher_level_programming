#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email."""

import requests
from sys import argv

if __name__ == "__main__":
    payload = {'email': argv[2]}

    r = requests.post(argv[1], data=payload)
    print(r.text)
