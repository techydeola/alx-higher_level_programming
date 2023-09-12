#!/usr/bin/python3

"""
This modules defines one function
"""
import json


def to_json_string(my_obj):
    """
        to_json_string - a function

        Return:
                JSON representation of an object
    """
    return json.dumps(my_obj)
