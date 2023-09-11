#!/usr/bin/python3

""" This module contains one function """


def is_kind_of_class(obj, a_class):
    """ This checks is an object is an instance
        of a class

        Returns:
                True if True
                otherwise: False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
