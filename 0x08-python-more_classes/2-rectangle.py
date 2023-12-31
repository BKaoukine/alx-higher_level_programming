#!/usr/bin/python3
"""A Rectangel Classe"""


class Rectangle:
    """Rectangle Classe"""

    def __init__(self, width=0, height=0):
        """initialization of instational

            args:
                width: width of the rectangle
                height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """This methode returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """This methode returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0

        else:
            return (self.__height + self.__width) * 2
