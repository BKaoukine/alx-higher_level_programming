#!/usr/bin/python3
"""Function that converts a string into a JSON."""
import json


def to_json_string(my_obj):
    """to_json_string taks one arg.

    my_obj: the object to convert.
    """
    serialize_obj = json.dumps(my_obj)
    return serialize_obj
