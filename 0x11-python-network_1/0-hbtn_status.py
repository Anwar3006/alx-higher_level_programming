#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""
from urllib.request import urlopen, Request


if __name__ == "__main__":
    req = Request('https://alx-intranet.hbtn.io/status')

    with urlopen(req) as response:
        data = response.read()
        content_decode = data.decode('UTF-8')

    print('Body Response:')
    print('\t type: {}'.format(type(data)))
    print('\t content: {}'.format(data))
    print('\t utf8 content: {}'.format(content_decode))
