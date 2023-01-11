#!/usr/bin/python3
# A function adds all unique integers in a list

def uniq_add(my_list=[]):
    # Get the unique values by using set() method
    unique_list = set(my_list)

    sum_int = 0
    for num in unique_list:
        sum_int += num
    return (sum_int)
