#!/usr/bin/python3
"""A Rectangel Classe"""


class Rectangle:
    """Rectangle Classe"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initialization of instational

            args:
                width: width of the rectangle
                height: height of the rectangle
        """
        self.width = width
        self.height = height
        self.number_of_instances += 1

    def __str__(self) -> str:
        """A string representation of the object created or the Classe"""
        result = ""
        if self.width == 0 or self.height == 0:
            return result

        for i in range(self.height):
            for j in range(self.width):
                result += "#"
            if i < self.height - 1:
                result += "\n"
        return result

    def __repr__(self) -> str:
        """returns a string representation of an object."""
        rp_rectangle = "Rectangle({}, {})".format(self.__width, self.__height)
        return rp_rectangle

    def __del__(self):
        """prints to STDOUT when an instance is to be deleted"""
        self.number_of_instances -= 1
        print("Bye rectangle...")

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
