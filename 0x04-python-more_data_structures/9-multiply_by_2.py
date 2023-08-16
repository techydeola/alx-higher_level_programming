#!usr/bin/python3
def multiply_by_2(a_dictionary):
    dict_new = dict(a_dictionary)
    for key in dict_new:
        dict_new[key] = dict_new[key] * 2
    return dict_new
