#!/usr/bin/python3
"""
this module define class call square
"""

class Square:
    """Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize square
        Args:
            size (int): square size.
            position (tuple): square position
        """
        self.size = size
        self.position = position

        if position[0] < 0 and position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

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

    @property
    def position(self):
        """position is a methode that gets the position attribute.

        Returns:
            returns position attribute

        """
        return self.__position

    @position.setter
    def position(self, value):
        """position is a methode that set the position attribute to value.

        args:
        value: the value to set position

        Returns:
            returns position attribute

        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        """Methode that prints the size attribute
        in #
        """
        if self.__size == 0:
            print()

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
