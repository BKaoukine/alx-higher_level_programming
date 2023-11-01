#!/usr/bin/python3

def islower(c):
    char_code = ord(c)
    if 97 >= char_code <= 122:
        return True
    else:
        return False
