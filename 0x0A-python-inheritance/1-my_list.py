#!/usr/bin/python3

"""
This module Inherits a class from parent class
"""


class MyList(list):
    def __init__(self):
        super().__init__(self)

    def print_sorted(self):
        """ this function prints the sorted list """
        print(sorted(self))
