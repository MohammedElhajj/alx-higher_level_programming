#!/usr/bin/python3
"""This module defines a function that prints  a text with 2 new
lines after: '.', '?' or ':'
"""


def text_indentation(text):
    """A function to print indented text

    Args:
        text(str): the text to be printed
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    idx = 0
    while idx < len(text) and text[idx] == ' ':
        idx += 1

    while idx < len(text):
        print(text[idx], end="")
        if text[idx] in ".?:" or text[idx] == "\n":
            if text[idx] in ".?:":
                print("\n")
            idx += 1
            while idx < len(text) and text[idx] == ' ':
                idx += 1
            continue
        idx += 1
