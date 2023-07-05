#!/usr/bin/python3
"""prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """ prints a text with 2 new lines after each of these characters: .,
    ? and :

    args:
        text: the text to print
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        if text[c] in ".?:":
            print("{}\n".format(text[c]))
            c += 2
        else:
            print(text[c], end="")
            c += 1
