#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_list = list(a_dictionary.keys())
    for value_list in keys_list:
        if value == a_dictionary.get(value_list):
            del a_dictionary[value_list]
    return a_dictionary
