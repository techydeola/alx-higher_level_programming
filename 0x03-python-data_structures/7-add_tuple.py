#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)

    if len_a == 1:
        tuple_a = tuple_a + (0,)
    if len_b == 1:
        tuple_b = tuple_b + (0,)
    if len_a == 0:
        tuple_a = (0, 0)
    if len_b == 0:
        tuple_b = (0, 0)

    sum_0 = tuple_a[0] + tuple_b[0]
    sum_1 = tuple_a[1] + tuple_b[1]

    result = (sum_0, sum_1)
    return result
