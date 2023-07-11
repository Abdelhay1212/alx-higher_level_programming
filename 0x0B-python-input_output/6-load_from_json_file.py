#!/usr/bin/python3
"""function that creates an Object from a "JSON file":
"""
import json


def load_from_json_file(filename):
    """returns an object"""
    with open(filename, "r", encoding="utf-8") as f:
        data = f.read()
    data = json.loads(data)
    return data
