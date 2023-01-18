#!/usr/bin/python3
"""Takes in a letter and sends a POST request
to `http://0.0.0.0:5000/search_user` with the
letter as a parameter and with `requests` module.
"""
import requests
from sys import argv

if __name__ == "__main__":
    q = argv[1]
    if q == "" or type(q) != str:
        print('No result')

    try:
        payload = {'q': q}
        r = requests.post('http://0.0.0.0:5000/search_user', payload).json()

        print('[{id}] {name}'.format(id=r.get('id'), name=r.get('name')))
    except ValueError:
        print('Not a valid JSON')
