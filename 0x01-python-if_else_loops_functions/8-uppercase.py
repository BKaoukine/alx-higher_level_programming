#!/usr/bin/python3
def uppercase(str):
    i = 0
    str_length = len(str)
    while i < str_length:
        if 97 <= ord(str[i]) <= 122:
            converter = 32
        else:
            converter = 0
        print("{:s}".format(chr((ord(str[i]) - converter))), end='')
        i += 1
    print("\n")
