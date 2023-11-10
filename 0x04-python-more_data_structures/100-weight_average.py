#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    result = 0
    div = 0
    for tup in my_list:
        result += tup[0] * tup[1]
        div += tup[1]
    result /= div
    return result
