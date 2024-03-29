#!/usr/bin/python3
"""Module to define the to_json_string function
"""


import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)
    Args:
        my_obj(str): the object to be handled
    """
    return json.dumps(my_obj)
