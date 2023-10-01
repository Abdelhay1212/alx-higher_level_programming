#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""


import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    try:
        with urllib.request.urlopen(url) as response:
            content = response.read()
            print("""Body response:
\t- type: {}
\t- content: {}""".format(type(str(content)), content.decode('utf-8')))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))