#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if matrix == [] or matrix is None:
        return

    MyList = []

    for i in matrix:
        NewList = list(map((lambda x: x**2), i))
        MyList.append(NewList)

    return MyList
