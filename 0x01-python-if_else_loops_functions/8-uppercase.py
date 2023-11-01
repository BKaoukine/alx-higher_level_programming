#!/usr/bin/python3
def uppercase(str):
    i = 0
    str_length = len(str)
    while i < str_length:
        separator = '' if i < str_length - 1 else "\n"
        if 97 <= ord(str[i]) <= 122:
            print("{:s}".format(chr((ord(str[i]) - 32))), end=separator)
        else:
            print("{:s}".format(str[i]), end=separator)
        i += 1
