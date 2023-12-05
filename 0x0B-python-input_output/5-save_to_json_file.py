#!/usr/bin/python3
"""Function that write a JSON obj into a file."""
import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file taks two arg.

    my_obj: the JSON string to write.
    filename: the file to write to.
    """
    serialize_obj = json.dumps(my_obj)
    with open(filename, "w") as _file:
        _file.write(serialize_obj)
