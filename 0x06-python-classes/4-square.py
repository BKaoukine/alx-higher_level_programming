#!/usr/bin/python3
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
        """Calculate and return the current square area."""
        return self.__size ** 2

    @property
    def size(self):
        """Get the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size attribute to value.
        Args:
            value: the value to set size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
