#!/usr/bin/python3

"""
This module supplies one function
    First function:
        add_integer:
            The function adds two integers
        Returns: The addition of the two integers
"""


def add_integer(a, b=98):
    """ Function that adds two integer and/or float numbers

    Args:
        a: first number
        b: second number

    Returns:
        The addition of the two given numbers

    Raises:
        TypeError: If a or b aren't integer and/or float numbers

    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    result = int(a + b)
    return result
