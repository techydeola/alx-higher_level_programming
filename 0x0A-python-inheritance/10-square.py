#!/usr/bin/python3

""" This module contains one class """


Rectangle = __import__('9-rectangle').Rectangle


class Square:
    """ This class inherits from Rectangle """
    def __init__(self, size):
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ this method claculates the area of a square """
        return self.__size * self.__size
