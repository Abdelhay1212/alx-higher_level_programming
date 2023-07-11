#!/usr/bin/python3
"""define a class"""


class MyList(list):
    """class MyList inherits from subclass list"""

    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """print the list sorted"""
        print(sorted(self))
