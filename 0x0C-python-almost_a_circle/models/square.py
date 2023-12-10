#!/usr/bin/python3
"""Square Class."""
from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """Class Constructor."""
        super().__init__(id, x, y)
        super().__init__(width=size)
        super().__init__(height=size)

    @property
    def width(self):
        return super().width

    @width.setter
    def width(self, size):
        if type(size) is not int:
            raise TypeError("width must be integer")
        if size <= 0:
            raise ValueError("width must be > 0")

        self.width = size

    @property
    def size(self):
        """Get the size."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size, assigning the same value to width and height."""

        if type(value) is not int:
            raise TypeError("width must be integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value
