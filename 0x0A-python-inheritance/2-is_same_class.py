#!/usr/bin/python3

""" This module contains one function """


def is_same_class(obj, a_class):
    """ This checks is an object is an instance
        of a class

        Returns:
                True if True
                otherwise: False
    """
    if type(obj) is a_class:
        return True
    else:
        return False
