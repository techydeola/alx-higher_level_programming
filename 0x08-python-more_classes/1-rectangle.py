#!/usr/bin/python3
"""
This module contains one function
"""


class Rectangle:
    """
    This class does nothing
    """
    def __init__(self, width=0, height=0):
        """
        This method initializes instances created
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ makes width a private attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets width with a value  """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ makes height a private attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets height with a value  """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
