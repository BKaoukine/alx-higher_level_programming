#!/usr/bin/python3
"""Square Class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Class Constructor."""
        super().__init__(id, x, y)
        super().__init__(width=size)
        super().__init__(height=size)

    @property
    def width(self):
        """Get the width."""
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

    def update(self, *args, **kwargs):
        """Update method to update the attributes."""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """To_dictionary Creates a dic representation of the Class."""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y,
        }
