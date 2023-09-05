#!/usr/bin/python3

"""
This module contains one function
    matrix divided - a fuction that peforms a division on
    each of the element in list of list
"""


def matrix_divided(matrix, div):
    """
    matrix_divided - divides all the elements in a list of lists and
                     returns a new lists
                Args:
                    matrix: a list of lists
                    div: value of the divisor
                Error checks:
                    - inconsistent list length
                    - invalid type
                    - zero div
                    - ivalid dive type
                Returns:
                    A new list of lists
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")
    list_comp = matrix[0]

    for lists in matrix:
        if len(lists) != len(list_comp):
            raise TypeError("Each row of the matrix must have the same size")
        for element in lists:
            if type(element) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists)" +
                                " of integers/floats")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    final_list = []
    for lists in matrix:
        new_list = []
        for element in lists:
            result = round(element / div, 2)
            new_list.append(result)

        final_list.append(new_list)

    return final_list
