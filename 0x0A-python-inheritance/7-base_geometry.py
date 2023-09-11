#!/usr/bin/python3

""" This module contains one class """


class BaseGeometry:
    """ BaseGeometry: a class
    """

    def area(self):
        """ a function that raises an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ this function validates the parameters"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
