#!/usr/bin/python3
"""function that reads a text file (UTF8) and prints it to stdout"""


def write_file(filename="", text=""):
    """ function that writes a string to a text file (UTF8)
    and returns the number of characters written

    args:
        filename: the file to write into
        text: message to write into the file
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    return len(text)
