#!/usr/bin/python3
def print_last_digit(number):
    _last_digit = number - (10 * int(number / 10))
    return _last_digit
