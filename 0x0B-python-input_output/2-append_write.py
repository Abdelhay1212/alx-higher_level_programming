#!/usr/bin/python3
"""function that appends a string at the end of a text file (UTF8)"""


def append_write(filename="", text=""):
    """ appends a string to a text file (UTF8)
    returns the number of characters added

    args:
        filename: the file to append to
        text: message to append into the file
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
    return len(text)
