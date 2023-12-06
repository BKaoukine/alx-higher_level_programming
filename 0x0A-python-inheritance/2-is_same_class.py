#!/usr/bin/python3
"""is_same_class."""


def is_same_class(obj, a_class):
    """is_same_class checks if the objects is instance of a class."""
    if isinstance(obj, a_class):
        return True
    else:
        return False
