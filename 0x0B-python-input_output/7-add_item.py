#!/usr/bin/python3

"""
This modules takes command line arguments and
appends it to a python list
"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

script_name = sys.argv[0]
script_arg = sys.argv[1:]

try:
    myList = (load_from_json_file('add_item.json'))
except FileNotFoundError:
    myList = []

myList.extend(script_arg)
save_to_json_file(myList, 'add_item.json')
