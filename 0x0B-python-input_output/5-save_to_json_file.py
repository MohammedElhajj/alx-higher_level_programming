#!/usr/bin/python3
"""Module to define the save_to_json_file function
"""


import josn


def save_to_json_file(my_obj, filename):
    """Function to write an Object to a text file
        using a JSON representation
    
    Args:
        my_obj(str): the object to be written
        filename(str): the text file to write to
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(json.dumps(my_obj))
