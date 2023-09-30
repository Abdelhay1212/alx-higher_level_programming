#!/usr/bin/python3
"""Sends a POST request to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)"""


import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    data = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(data).encode('ascii')

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        content = response.read()
        print(content.decode('utf-8'))
