#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_num = 0
    for item in my_list[:x]:
        try:
            print("{:d}".format(item), end="")
            printed_num += 1

        except (ValueError, TypeError):
            pass
    print()
    return printed_num
