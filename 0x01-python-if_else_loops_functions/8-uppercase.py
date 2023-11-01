#!/usr/bin/python3
def uppercase(str):
    i = 0
    str_length = len(str)
    while i < str_length:
        if 97 <= ord(str[i]) <= 122:
            print("{:s}".format(chr((ord(str[i]) - 32))), end='')
        else:
            print("{:s}".format(str[i]), end='')
        i += 1
