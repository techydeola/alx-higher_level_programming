#!/usr/bin/python3

""" This module contains one function """


def inherits_from(obj, a_class):
    """ This checks is an object is an inheritance
        of a class

        Returns:
                True if True
                otherwise: False
    """
    if type(obj) is not a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
