#!/usr/bin/python3
"""Defines a class Base
"""


class Base:
    """
    Base class with a unique ID assigned to each instance.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance with a unique ID.

        If an ID is provided, it is assigned to the instance.
        Otherwise, the next available ID is assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
