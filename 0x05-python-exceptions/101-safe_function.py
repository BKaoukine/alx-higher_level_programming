#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as execerr:
        print("Exception: {}".format(execerr), file=sys.stderr)
        return None
