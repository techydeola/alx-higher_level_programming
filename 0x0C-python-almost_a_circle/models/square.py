#!/usr/bin/python3
"""
    This modules contains an inheritance class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ this class inherits from the rectangle class """

    def __init__(self, size, x=0, y=0, id=None):

        """ initializing method """
        super().__init__(size, size, x=x, y=y, id=id)

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        square_size = super().width
        x = super().x
        y = super().y
        return f"[Square] ({self.id})" + " " + \
            f"{x}/{y} - {square_size}"

    @property
    def size(self):
        """ returns the size attribute """
        return super().width

    @size.setter
    def size(self, value):
        """ setter for size attribute """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ this method updates intances """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ this method returns the dictionary representation
            of a rectangle
        """
        return {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y
            }
