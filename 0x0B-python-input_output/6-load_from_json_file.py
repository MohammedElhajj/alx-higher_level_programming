#!/usr/bin/python3
"""Module to define the load_from_json_file function
"""


import json


def load_from_json_file(filename):
    """Function to create an Object from a “JSON file”

    Args:
        filename(str): the JSON file to create an object from
    """
    with open(filename, encoding='utf-8') as file:
        return json.loads(file.read())
