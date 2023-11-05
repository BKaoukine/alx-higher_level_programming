#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list_len = len(my_list) - 1
    if idx > my_list_len or idx < 0:
        return my_list
    else:
        my_new_list = my_list.copy()
        my_new_list[idx] = element
        return my_new_list
