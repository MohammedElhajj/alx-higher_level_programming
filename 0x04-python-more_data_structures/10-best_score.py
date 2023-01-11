#!/usr/bin/python3
# A function returns a key with the biggest integer value

def best_score(a_dictionary):
    # Get the corresponding key by passing in key=dictionary.get to max()
    # Return None if no score found
    return (max(a_dictionary, key=a_dictionary.get) if a_dictionary else None)
