#!/usr/bin/python3
"""BaseGeometry class."""


class BaseGeometry:
    """BaseGeometry."""

    def area(self):
        """Area method."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method that validates an integer value.

        Args:
            name (str): The name of the variable.
            value (int): The value of the variable.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")