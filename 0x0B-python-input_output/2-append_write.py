#!/usr/bin/python3

"""
This modules defines one function that appends to a file
"""


def append_write(filename="", text=""):
    """
        write_file - appends a text to a file

        Return:
                number of characters written
    """
    with open(filename, mode="a", encoding='utf-8') as myFile:
        return myFile.write(text)
