#!/usr/bin/python3
"""Function that creates an Object from a 'JSON file'."""
import json


def load_from_json_file(filename):
    """load_from_json_file taks one arg.

    filename: the JSON file.
    """
    with open(filename, "r") as json_file:
        json.load(json_file)
