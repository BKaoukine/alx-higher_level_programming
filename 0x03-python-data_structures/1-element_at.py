#!/usr/bin/python3
def element_at(my_list, idx):
    my_list_len = len(my_list) - 1
    if idx > my_list_len or idx < 0:
        return None
    else:
        return my_list[idx]
