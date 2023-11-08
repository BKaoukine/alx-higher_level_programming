#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_list_len = len(my_list)
    index = 0
    while index < my_list_len:
        if my_list[index] == search:
            my_list[index] = replace
        index += 1
        
    return my_list
