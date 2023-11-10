#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for keys in a_dictionary:
        if keys == key:
            a_dictionary.pop(key)
            return a_dictionary
    return a_dictionary
