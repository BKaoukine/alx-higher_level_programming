#!/usr/bin/python3
"""
Function that returns a list of available.

attributes and methods of an object.
"""


def lookup(obj):
    """Lookup take one argument.

    obj: the object in search.
    """
    return dir(obj)
