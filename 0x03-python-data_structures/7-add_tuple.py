#!/usr/bin/python3
# A function that adds 2 tuples

def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    # Use the first two integers only in the addition
    # And use the value 0 for each mising integer with them
    tuple_1 = tuple_a + (0, 0)
    tuple_2 = tuple_b + (0, 0)
    new_tuple = tuple_1[0] + tuple_2[0], tuple_1[1] + tuple_2[1]
    return new_tuple
