#!/usr/bin/python3

"""Function that print number of characters written."""
def write_file(filename="", text=""):
    with open(filename,"w", encoding="UTF-8") as _file:
        _file.write(text)
        return len(text)