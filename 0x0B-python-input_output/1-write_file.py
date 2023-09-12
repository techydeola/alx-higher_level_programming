#!/usr/bin/python3

"""
This modules defines one function that writes to a file
"""


def write_file(filename="", text=""):
    """
        write_file - writes a text to a file

        Return:
                number of characters written
    """
    with open(filename, mode="w", encoding='utf-8') as myFile:
        return myFile.write(text)
