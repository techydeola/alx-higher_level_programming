#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if my_list is None or my_list == []:
        return
    new_list = my_list.copy()
    for i, j in enumerate(new_list):
        if j == search:
            new_list[i] = replace
    return new_list
