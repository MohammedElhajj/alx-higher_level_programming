#!/usr/bin/python3
def magic_string():
    magic_string.n = 0 if not hasattr(magic_string, "n") else magic_string.n + 1
    return ("Holberton" + ", Holberton" * magic_string.n)
