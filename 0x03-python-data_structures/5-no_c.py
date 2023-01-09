#!/usr/bin/python3
# A function to remove all characters c and C from a string

def no_c(my_string):
    new_string = my_string.translate({ord(i): None for i in 'cC'})
    # Using translate() method to remove the multiple characters
    return new_string
