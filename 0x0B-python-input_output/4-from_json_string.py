#!/usr/bin/python3
"""Function that converts a JSON string into a python obj."""
import json


def from_json_string(my_str):
    """from_json_string taks one arg.

    my_str: the JSON string to convert.
    """
    deserialize_obj = json.loads(my_str)
    return deserialize_obj
