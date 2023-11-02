#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    i = len(argv)
    n = 0
    j = 1
    if i == 1:
        print("{:d} arguments.".format(i-1))

    elif i == 2:
        print("{:d} argument:".format(i-1))
        print("{:d}: {:s}".format(j, argv[j]))
    elif i > 1:
        print("{:d} arguments:".format(i-1))

        while n+1 < i:
            print("{:d}: {:s}".format(j, argv[n+1]))
            n += 1
            j += 1
