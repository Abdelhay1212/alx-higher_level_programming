#!/usr/bin/python3
"""Defines a class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square that inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initilize attributes size ,x, y and id
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get/set the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates the attributes of a Square instance"""
        if args and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.size = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
        else:
            if kwargs and len(kwargs) != 0:
                for k, v in kwargs.items():
                    if k == "id":
                        self.id = v
                    elif k == "size":
                        self.width = v
                    elif k == "x":
                        self.x = v
                    elif k == "y":
                        self.y = v

    def __str__(self):
        """return [Square] (<id>) <x>/<y> - <size>"""
        s1 = "{}".format(self.id)
        s2 = "{}/{} - {}".format(self.x, self.y, self.width)
        return "[Square] ({}) {}".format(s1, s2)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y,
        }
