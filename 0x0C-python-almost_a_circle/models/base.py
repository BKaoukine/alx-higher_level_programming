#!/usr/bin/python3
"""Base class."""


class Base:
    """Private Attribute to keep track of base instances."""

    __nb_objects = 0

    def __init__(self, id=None):
        """__init__ class constructor."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
