#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    list_len = 0
    printed_num = 0
    for num in my_list:
        list_len += 1
    try:
        if x > list_len:
            while printed_num <= list_len - 1:
                print("{}".format(my_list[printed_num]), end="")
                printed_num += 1
            print()
        elif x < list_len:
            while printed_num <= x - 1:
                print("{}".format(my_list[printed_num]), end="")
                printed_num += 1
            print()
        elif x == list_len:
            while printed_num <= list_len - 1:
                print("{}".format(my_list[printed_num]), end="")
                printed_num += 1
            print()
        return printed_num
    except Exception:
        return list_len
