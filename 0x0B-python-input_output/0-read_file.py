#!/usr/bin/python3
"""Function that opens a file and read it's contecnt."""


def read_file(filename=""):
    """Open the filename as file."""
    with open(filename, "r", encoding="utf-8") as file:
        """Reade the file."""
        file.read()
