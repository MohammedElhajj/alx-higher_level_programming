#!/usr/bin/python3
"""Module to define the write_file function
"""


def write_file(filename="", text=""):
    """Function to write a string to a text file (UTF8

    Args:
        filename(str): the text file
        text(str): the string to be written
    Returns:
        The number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
