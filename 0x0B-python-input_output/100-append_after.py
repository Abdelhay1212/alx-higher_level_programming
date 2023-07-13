#!/usr/bin/python3
"""function that inserts a line of text to a file,
after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file,
    after each line containing search_string

    args:
        filename: the file to insert to
        search_string: inserts after this string
        new_string: string to insert
    """
    string = ""
    with open(filename, 'r') as file:
        for line in file:
            string += line
            if search_string in line:
                string += new_string

    with open(filename, 'w') as file:
        file.write(string)
