#!/usr/bin/python3
"""inherits_from."""


def inherits_from(obj, a_class):
    """inherits_from checks if the objects is instance of a class."""
    if isinstance(type(obj), a_class):
        return True
    else:
        return False
