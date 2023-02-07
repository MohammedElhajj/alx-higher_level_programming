#!/usr/bin/python3
"""Module to define the from_json_string function
"""


import json


def from_json_string(my_str):
    """Returns the python object representation of a JSON string
    Args:
        my_str(str): the string to be represented
    """
    return json.loads(my_str)
