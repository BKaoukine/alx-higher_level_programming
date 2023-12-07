#!/usr/bin/python3
"""A class that inherits from Rectangle."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size):
        """__init__ methode."""
        self.integer_validator(self, size)
        self.__size = size

    def area(self):
        """Area method."""
        return self.__size * self.__size
