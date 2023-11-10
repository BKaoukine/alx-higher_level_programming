#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Iterate through the sorted key-value pairs and print them
    for key, value in sorted(a_dictionary.items()):
        print("{} : {}".format(key, value))

