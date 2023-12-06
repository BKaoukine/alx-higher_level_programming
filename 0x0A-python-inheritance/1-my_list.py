#!/usr/bin/python3
"""MyList Class."""


class MyList(list):
    """class."""

    def print_sorted(self):
        """print_sorted method sorts a list of all.

        available methodes and attributes  of the class.
        """
        sort_list = dir(self)
        sort_list.sort()
        print(sort_list)
