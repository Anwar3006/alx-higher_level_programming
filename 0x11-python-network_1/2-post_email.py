#!/usr/bin/python3
""" """

if __name__ == "__main__":
    from urllib import request, parse
    from sys import argv

    data = argv[2]

    data = parse.urlencode(
        {'email': data}).encode('ascii')

    req = request.Request(argv[1], data)
    with request.urlopen(req) as response:
        page = response.read()

    print(page.decode('utf-8'))
