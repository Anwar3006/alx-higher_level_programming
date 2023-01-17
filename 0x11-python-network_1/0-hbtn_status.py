#!/usr/bin/python3
""" """
from urllib.request import urlopen


if __name__ == "__main__":
    with urlopen('https://alx-intranet.hbtn.io/status') as response:
        data = response.read()
        content_decode = data.decode('UTF-8')

    print('Body Response:')
    print('\t type: {}'.format(type(data)))
    print('\t content: {}'.format(len(data)))
    print('\t utf8 content: {}'.format(content_decode))
