#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list == None:
        return
    index = len(my_list) - 1

    while index != -1:
        print("{:d}".format(my_list[index]))
        index -= 1
