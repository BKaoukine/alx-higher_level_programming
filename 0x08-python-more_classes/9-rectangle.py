#!/usr/bin/python3
"""A Rectangel Classe"""


class Rectangle:
    """Rectangle Classe"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialization of instational

            args:
                width: width of the rectangle
                height: height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self) -> str:
        """A string representation of the object created or the Classe"""
        if self.__width == 0 or self.__height == 0:
            return ""
        ps = str(self.print_symbol)
        return '\n'.join([ps * self.__width for _ in range(self.__height)])

    def __repr__(self) -> str:
        """returns a string representation of an object."""
        rp_rectangle = "Rectangle({}, {})".format(self.__width, self.__height)
        return rp_rectangle

    def __del__(self):
        """prints to STDOUT when an instance is to be deleted"""
        Rectangle.number_of_instances -= 1
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Methode that compares two instances and returns the bigger one"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_2.area() == rect_1.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """Methode that creates a new instance of Rectangle and
        sets the widthe and height value to size

        args:
            size : the size to set width and height
        """
        return cls(size, size)
