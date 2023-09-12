#!/usr/bin/python3

"""
This modules defines one function
"""
import json


def from_json_string(my_str):
    """
        to_json_string - a function

        Return:
                JSON representation of a string
    """
    return json.loads(my_str)
