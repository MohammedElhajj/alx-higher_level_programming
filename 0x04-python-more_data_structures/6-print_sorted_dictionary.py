#!/usr/bin/python3
# A function prints a dictionary by ordered keys

def print_sorted_dictionary(a_dictionary):
    # Sort the keys alphabetically by using sorted()
    for key, value in sorted(a_dictionary.items()):
        print("{}: {}".format(key, value))
