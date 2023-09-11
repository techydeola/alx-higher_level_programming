#!/usr/bin/python3

"""
This module Inherits a class from parent class
"""


class MyList(list):
    """ MyList is a class that inherits """
    def print_sorted(self):
        """ this function prints the sorted list """
        print(sorted(self))
