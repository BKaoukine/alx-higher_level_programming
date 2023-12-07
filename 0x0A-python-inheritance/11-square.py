#!/usr/bin/python3
"""A class that inherits from Rectangle."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size):
        """__init__ methode."""
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """ __str__ method """
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """Area method."""
        return self.__size * self.__size
