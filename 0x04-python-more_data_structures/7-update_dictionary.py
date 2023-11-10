#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for keys, values in a_dictionary.items():
        if keys == key:
            a_dictionary[keys] = value
        else:
            a_dictionary[key] = value
            break
