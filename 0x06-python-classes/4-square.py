#!/usr/bin/python3
"""square class"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """Initialize square
        Args:
            size (int): square size.
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """area is a methode that calculates the current area
        based on given size.

        Returns:
            returns the current square area

        """
        return self.__size ** 2

    @property
    def size(self):
        """size is a methode that gets the size attribute.

        Returns:
            returns size attribute

        """
        return self.__size

    @size.setter
    def size(self, value):
        """size is a methode that set the size attribute to value.

        args:
        value: the value to set size

        Returns:
            returns size attribute

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
