#!/usr/bin/python3

i = 0

while i <= 99:
    if i < 10:
        separator = ", "
        print("0{:d}".format(i), end=separator)
    else:
        separator = ", " if i != 99 else "\n"
        print("{:d}".format(i), end=separator)
    i += 1
