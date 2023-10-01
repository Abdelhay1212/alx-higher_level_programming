#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter."""


import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    data = {'q': "" if len(sys.argv) == 1 else sys.argv[1]}

    r = requests.post(url, data)
    try:
        valid_json = r.json()
        if valid_json == {}:
            print("No result")
        else:
            print("[{}] {}".format(valid_json.get("id"),
                                   valid_json.get("name")))
    except ValueError:
        print("Not a valid JSON")
