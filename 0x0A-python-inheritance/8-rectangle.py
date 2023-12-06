#!/usr/bin/python3
"""Rectangle class."""
basegeometry = __import__('7-base_geometry').basegeometry


class Rectangle(basegeometry.BaseGeometry):
    """Rectangle class that inherits from basegemotry classe."""

    def __init__(self, width, height):
        """Initalisation.

        arg:
        width : width of the rectangle.
        height : height of the rectangle.
        """
        if basegeometry.integer_validator("width", width):
            self.__width = width
        if basegeometry.integer_validator("height", height):
            self.__height = height
