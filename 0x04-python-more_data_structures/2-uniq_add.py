#!/usr/bin/python3

def uniq_add(my_list=[]):
    if my_list is None or my_list == []:
        return

    new_list = set(my_list)
    sum = 0

    for i in new_list:
        sum += i

    return sum
