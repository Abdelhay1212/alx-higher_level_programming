#!/usr/bin/python3
"""function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """Prints the content of a file
    args:
        filename: the file to print its content
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
