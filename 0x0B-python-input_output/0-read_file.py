#!/usr/bin/python3
"""Module to define the read_file function"""


def read_file(filename=""):
    """Function to read a text file and print it to stdout
    Args:
        filename(str): the file name
    """
    with open(filename, encoding='utf-8') as file:
        for line in file:
            print(line, end="")
