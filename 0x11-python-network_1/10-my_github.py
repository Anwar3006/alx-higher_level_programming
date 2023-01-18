#!/usr/bin/python3
"""Takes my Github credentials (username and token)
and uses the Github API to display my Github id."""

import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    git_uri = 'https://api.github.com/users/' + username

    response = requests.get(git_uri, auth=(username, token))

    data = response.json()

    print(data.get('id'))
