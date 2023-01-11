#!/usr/bin/python3
# A function deletes a key in a dictionary

def simple_delete(a_dictionary, key=""):
    a_dictionary.pop(key, None)
    # Using pop() method with no value to be returned if
    # a key cannot be found
    return (a_dictionary)
