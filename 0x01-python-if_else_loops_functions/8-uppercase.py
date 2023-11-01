#!/usr/bin/python3

def uppercase(input_str):
    i = 0
    str_length = len(input_str)
    result_str = ""

    while i < str_length:
        if 97 <= ord(input_str[i]) <= 122:
            converter = 32
        else:
            converter = 0
        result_str += chr(ord(input_str[i]) - converter)
        i += 1

    print("{:s}".format(result_str))
