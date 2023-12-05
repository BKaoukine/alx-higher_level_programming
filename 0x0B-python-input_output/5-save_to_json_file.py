#!/usr/bin/python3
"""Function that write a JSON obj into a file."""
import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file taks two arg.

    my_obj: the JSON string to write.
    filename: the file to write to.
    """
    with open(filename, "w") as json_file:
        json.dump(my_obj, json_file)
