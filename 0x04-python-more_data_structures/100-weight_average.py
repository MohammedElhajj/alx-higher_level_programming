#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list: 
        # Weighted_avg = sum(i*j)/sum(j) i: int number, j: weighting factor
        return (sum(i * j for i, j in my_list) / sum(j for i, j in my_list))
    return (0) # If the list is empty
