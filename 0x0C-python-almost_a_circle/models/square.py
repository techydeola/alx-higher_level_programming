#!/usr/bin/python3

"""
    This modules contains an inheritance class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ this class inherits from the rectangle class """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        square_size = super().width
        x = super().x
        y = super().y
        return f"[Square] ({self.id})" + " " + \
            f"{x}/{y} - {square_size}"
    
    @property
    def size(self):
        return super().width
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
