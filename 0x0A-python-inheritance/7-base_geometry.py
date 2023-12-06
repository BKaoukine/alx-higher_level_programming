#!/usr/bin/python3
"""BaseGeometry class."""


class BaseGeometry:
    """BaseGeometry."""

    def area(self):
        """Area method."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integer validator takes two arg.
        
        name : name of the variable.
        value : value of the variable.
        """
        self.name = name
        self.value = value
        if self.value != int:
            raise TypeError("<name> must be an integer")
        if self.value <= 0:
            raise ValueError("<name> must be greater than 0")
