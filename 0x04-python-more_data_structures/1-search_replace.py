#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_list_len = len(my_list)
    index = 0
    new_list = my_list
    while index < my_list_len:
        if my_list[index] == search:
            new_list[index] = replace
        index += 1
        
    return new_list
