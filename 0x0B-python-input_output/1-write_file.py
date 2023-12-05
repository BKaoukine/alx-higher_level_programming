#!/usr/bin/python3
"""Function that print number of characters written."""


def write_file(filename="", text=""):
    """write_file Function.

    param:
    filename: the file name to write to
    text: the text to write to the file
    """
    with open(filename, "w", encoding="UTF-8") as _file:
        _file.write(text)
        return len(text)
