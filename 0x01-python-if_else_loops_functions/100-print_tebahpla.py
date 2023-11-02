#!/usr/bin/python3
i = 122
while i > 96:
    if i % 2 != 0:
        num = 32
    else:
        num = 0
    print("{}".format(chr(i - num)), end="")
    i -= 1
