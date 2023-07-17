#!/usr/bin/python3
"""Defines a class Rectangle
"""


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
        self.__width = value

    @property
    def height(self):
        """get/set the height of the rectange"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """get/set the attr x of the rectange"""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """get/set the attr y of the rectange"""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
