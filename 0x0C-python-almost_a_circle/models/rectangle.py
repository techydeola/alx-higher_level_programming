#!/usr/bin/python3

"""
    This module contains a class that inherits
    from the Base class
"""


from models.base import Base


class Rectangle(Base):
    """ this class inherits the base class """
    def __init__(self, width, height, x=0, y=0, id=None):

        """ width instantiation validation """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

        """ height instantiation validation """
        if not isinstance(height, int):
            raise TypeError("width must be an integer")
        if height <= 0:
            raise ValueError("width must be > 0")

        """ x instantiation validation """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

        """ y instantiation validation """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

        """ calling the properties of the Base class """
        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def update(self, *args, **kwargs):
        """ updates instance attribute based on the number of
            of argument given.
        """

        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    @property
    def width(self):
        return self.__width

    """width setter method """
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    """height setter method """
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    """x setter method """
    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    """y setter method """
    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ this function returns the area of a rectangle """
        return self.__width * self.__height

    def display(self):
        """ this function prints the rectangle instances
            as a "#" character
        """
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        return f"[Rectangle] ({self.id})" + " " + \
            f"{self.__x}/{self.__y} - {self.__width}/{self.__height}"
