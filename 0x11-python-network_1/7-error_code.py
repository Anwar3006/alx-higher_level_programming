#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body.
Usage: ./3-error_code.py <URL>
  - Handles HTTP errors. 
"""
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get(argv[1])

    if r.status_code >= 400:
        print('Error code:', r.status_code)
    else:
        print(r.text)
