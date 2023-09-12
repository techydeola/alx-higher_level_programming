#!/usr/bin/python3

"""
This modules defines one function
"""
import json


def load_from_json_file(filename):
    """
        to_json_string - a function that creates an object
                         froma JSON file

        Return:
                nothing
    """

    with open(filename, encoding="utf-8") as myFile:
        return json.loads(myFile.read())
