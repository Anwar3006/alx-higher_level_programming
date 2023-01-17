#!/usr/bin/python3
""" """
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        data = response.read()
        content_decode = data.decode('UTF-8')

    print('Body Response:')
    print('\t type: {}'.format(type(data)))
    print('\t content: {}'.format(len(data)))
    print('\t utf8 content: {}'.format(content_decode))
