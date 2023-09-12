#!/usr/bin/python3

"""
This modules defines one function
"""
import json


def save_to_json_file(my_obj, filename):
    """
        to_json_string - a function that writes a json object
                         into a file

        Return:
                nothing
    """

    with open(filename, mode="w", encoding="utf-8") as myFile:
        myFile.write(json.dumps(my_obj))
