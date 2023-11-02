#!/usr/bin/python3
from sys import argv
if len(argv) == 1:
    print("{:d}".format(0))
else:
    i = 1
    result = 0
    while i < len(argv):
        int_argv = int(argv[i])
        result += int_argv
        i += 1
    print("{:d}".format(result))
