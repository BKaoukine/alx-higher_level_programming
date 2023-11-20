#!/usr/bin/python3
def safe_print_integer(value):
    val_to_print = value
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
