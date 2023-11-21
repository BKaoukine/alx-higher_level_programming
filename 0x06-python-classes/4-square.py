#!/usr/bin/python3
"""square class"""


class Square:
    """square class"""
    def __init__(self, size=0):
        """init square
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
        self.area = self.__size * self.__size
        return self.area

    def size(self):
        """size is a methode that gets the size attribute.

        Returns:
            returns size attribute

        """
        return self.size

    def size(self, value):
        """size is a methode that set the size attribute to value.

        args:
        value: the value to set size

        Returns:
            returns size attribute

        """
        self.size = value
