#!/usr/bin/python3
if __name__ == "__main__":
    """
    This script prints the sum of 1 and 2
    using the 'add' function from add_0.py.
    """

    from add_0 import add
    a = 1
    b = 2

    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
