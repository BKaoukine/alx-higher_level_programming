#!/usr/bin/python3
"""Function that Appends text to a file."""


def append_write(filename="", text=""):
    """Append_write function take two arg.

    param:
    filename: the file to write to
    text: text to append to the file
    """
    with open(filename, "a", encoding="UTF-8") as _file:
        _file.write(text)
        return len(text)
