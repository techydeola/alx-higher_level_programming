#!/usr/bin/python3

"""
    This module contains one function
"""
import json


def class_to_json(obj):
    """
        class_to_json: a function that returns the dictionary
        description with simple data structure
        (list, dictionary, string, integer and boolean) for
        JSON serialization of an object:
    """
    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
