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

    def area(self):
        """ function that returns area of a rectangle """
        return self.height * self.width

    def perimeter(self):
        """ function that returns perimeter of a rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """ return the rectangle with the character #
        """
        if self.__width is 0 or self.__height is 0:
            return ""
        return ("\n".join(["".join(["#" for i in range(self.__width)])
                for j in range(self.__height)]))

    def __repr__(self):
        """ returns a srting representation """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """ prints a message wehn an instance is deleted """
        print("Bye rectangle...")
