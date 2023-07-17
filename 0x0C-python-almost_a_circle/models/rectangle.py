#!/usr/bin/python3
"""Defines a class Rectangle
"""
from base import Base


class Rectangle(Base):
    """
    class Rectangle that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle instance with attributes:
        width, height, x, y, id
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """get/set the width of the rectange"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get/set the height of the rectange"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get/set the attr x of the rectange"""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get/set the attr y of the rectange"""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the Rectangle instance"""
        return self.width * self.height

    def display(self):
        """Prints the Rectangle instance with caracter #"""
        [print() for i in range(self.y)]
        [print(" " * self.x + "#" * self.width) for i in range(self.height)]

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        s1 = "{}/{}".format(self.x, self.y)
        s2 = "{}/{}".format(self.width, self.height)
        return "[Rectangle] ({}) {} - {}".format(self.id, s1, s2)

    def update(self, *args, **kwargs):
        """updates the attributes of a Rectangle instance"""
        if args and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                elif i == 2:
                    self.height = args[i]
                elif i == 3:
                    self.x = args[i]
                elif i == 4:
                    self.y = args[i]
        else:
            if kwargs and len(kwargs) != 0:
                for k, v in kwargs.items():
                    if k == "id":
                        self.id = v
                    elif k == "width":
                        self.width = v
                    elif k == "height":
                        self.height = v
                    elif k == "x":
                        self.x = v
                    elif k == "y":
                        self.y = v
