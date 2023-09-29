#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request


url = "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(url) as response:
    content = response.read()
    utf8_content = content.decode('utf-8')


print("""Body response:$
\t- type: {}
\t- content: {}
\t- utf8 content: {}""".format(type(content), content, utf8_content))
