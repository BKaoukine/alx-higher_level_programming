#!/usr/bin/python3
"""Square Class."""
from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """Class Constructor."""
        super().__init__(id, x, y)
        super().__init__(width=size)
        super().__init__(height=size)
