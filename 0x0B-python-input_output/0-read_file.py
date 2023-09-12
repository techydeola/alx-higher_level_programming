#!/usr/bin/python3

"""
This modules defines one function that reads a file
"""


def read_file(filename=""):
    """ this function reads a file and prints it to stdout """
    with open(filename, encoding='UTF-8') as myFile:
        print(myFile.read())
