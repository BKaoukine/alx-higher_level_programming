#!/usr/bin/python3
def uniq_add(my_list=[]):

    uniq = set(my_list)
    stored = 0
    for i in uniq:
        stored += i
    return stored
