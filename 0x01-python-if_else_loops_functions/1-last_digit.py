#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def last_digit(number):
    _last_digit = number - (10 * int(number / 10))
    if _last_digit > 5:
        print("Last digit of {} is {} and is greater than 5"
              .format(number, _last_digit))
    elif _last_digit == 0:
        print("Last digit of {} is {} and is 0"
              .format(number, _last_digit))
    else:
        print("Last digit of {} is {} and is less than 6 and not 0"
              .format(number, _last_digit))


last_digit(number)
