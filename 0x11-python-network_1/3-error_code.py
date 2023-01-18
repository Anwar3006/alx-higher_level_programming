#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body.
Usage: ./3-error_code.py <URL>
  - Handles HTTP errors.
"""
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from sys import argv

if __name__ == "__main__":

    req = Request(argv[1])

    try:
        with urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
