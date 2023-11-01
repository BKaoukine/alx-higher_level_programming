#!/usr/bin/python3
def uppercase(str):
    i = 0
    while str:
        if 65 <= ord(str[i]) <= 90:
            print("{:s}".format(chr((ord(str[i]) + 32))), end='')
        else:
            print("{:s}".format(str[i]), end='')
        i += 1
    print("\n")
