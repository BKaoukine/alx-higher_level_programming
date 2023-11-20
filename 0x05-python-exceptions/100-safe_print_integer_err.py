#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    val_to_print = value
    try:
        print("{:d}".format(val_to_print))
        return True
    except ValueError as valerr:
        print(valerr, file=sys.stderr)
        return False
    except TypeError as typerr:
        print(typerr, file=sys.stderr)
        return False
