#!/usr/bin/python3
"""Define a function"""


def lookup(obj):
    """ returns the list of available attributes and methods of an object
    args:
        obj: class object
    """
    return dir(obj)
