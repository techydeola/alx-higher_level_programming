#!/usr/bin/python3
""" LockedClass
"""


class LockedClass:
    def __setattr__(self, name, value):
        if name == "first_name":
            super().__setattr__(name, value)
        else:
            raise AttributeError("You can only create 'first_name' attribute.")
