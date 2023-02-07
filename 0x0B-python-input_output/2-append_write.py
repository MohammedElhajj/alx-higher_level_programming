#!/usr/bin/python3
"""Module to define the append_write function
"""


def append_write(filename="", text=""):
    """Function to append a str at the end of a text file (UTF8)

    Args:
        filename(str): the text file
        text(str): the string to be appended
    Returns:
        The number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
