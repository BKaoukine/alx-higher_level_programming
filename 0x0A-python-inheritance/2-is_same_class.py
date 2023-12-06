#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    Function checks if the objects is instance of a class.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
