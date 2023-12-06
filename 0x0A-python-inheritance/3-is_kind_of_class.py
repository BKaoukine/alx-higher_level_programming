#!/usr/bin/python3
"""is_kind_of_class."""


def is_kind_of_class(obj, a_class):
    """is_kind_of_class checks if the objects is instance of a class."""
    if isinstance(type(obj), a_class):
        return True
    else:
        return False
