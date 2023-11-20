#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_num = 0
    try:
        for item in my_list:
            if type(item) is int:
                if printed_num <= x - 1:
                    print("{:d}".format(item), end="")
                    printed_num += 1
        print()
        return printed_num
    except (ValueError, TypeError, IndexError):
        return printed_num
