#!/usr/bin/python3
"""Base class."""
import json


class Base:
    """Private Attribute to keep track of base instances."""

    __nb_objects = 0

    def __init__(self, id=None):
        """__init__ class constructor."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Method that returns JSON representation fo list dict."""

        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """Method tha saves the JSON list_objs to a file."""

        with open(f"{cls.__name__}.json", "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                jsonfile.write(cls.to_json_string(list_objs))

    def from_json_string(json_string):
        """Method that returns the list of the JSON string representation."""
        if json_string is None:
            return "[]"
        else:
            return json.loads(json_string)

    def create(cls, **dictionary):
        """Method returns an instance with all attributes already set."""

        if cls.__name__ == 'Rectangle':
            new_instance = cls(1, 1)
        elif cls.__name__ == 'Square':
            new_instance = cls(1)

        new_instance.update(**dictionary)
        return new_instance
