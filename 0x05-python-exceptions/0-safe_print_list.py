#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    elements = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            elements += 1
        except Exception as e:
            pass
    print()
    return elements
