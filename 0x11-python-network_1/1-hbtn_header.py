#!/usr/bin/python3
"""Sends a request to the URL and displays the value of the X-Request-Id
variable found in the header of the response."""


if __name__ == "__main__":
    import urllib.request
    import sys

    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        data = response.info()

        print(data['X-Request-Id'])
