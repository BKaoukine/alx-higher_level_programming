#!/usr/bin/python3
"""Rectangle Class."""

from base import Base


class Rectangle(Base):
    """Rectangle Class that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor."""
        super().__init__(id)  # Initialize the base class with the provided id
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return (
            "[Rectangle] (" + str(self.id) + ") " +
            str(self.x) + "/" + str(self.y) + " - " +
            str(self.width) + "/" + str(self.height)
        )

    @property
    def width(self):
        """Get width."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """Get height."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get x."""
        return self.__x

    @x.setter
    def x(self, value):
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get y."""
        return self.__y

    @y.setter
    def y(self, value):
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        """Print the Rectangle instance with the character '#'."""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def update(self, *args, **kwargs):
        """Assign arguments to each attribute."""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Method that returns a dic representation of the Class"""
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
        }
