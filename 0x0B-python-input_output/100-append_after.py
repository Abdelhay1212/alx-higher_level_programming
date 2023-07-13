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
    with open(filename, 'r', encoding="utf-8") as file:
        lines = file.readlines()
        for i in range(len(lines)):
            if search_string in lines[i]:
                lines.insert(i + 1, new_string)

    with open(filename, 'w', encoding="utf-8") as file:
        for line in lines:
            file.write(line)
