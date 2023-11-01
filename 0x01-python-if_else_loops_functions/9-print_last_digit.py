#!/usr/bin/python3
def print_last_digit(number):
    _last_digit = abs(number - (10 * int(number / 10)))
    print("{:d}".format(_last_digit), end='')
    return _last_digit
