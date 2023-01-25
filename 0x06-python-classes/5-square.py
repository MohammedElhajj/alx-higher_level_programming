#!/usr/bin/python3
"""A module to create a class named Square"""


class Square:
    """A class named Square"""
    def __init__(self, size=0):
        """Initialize the new class Square
        Args:
        size(int): the size of the square
        """
        self.__size = size

    def area(self):
        """Calculate the area of the square
        Returns:
        the current square area
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """Get the current size of the class"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set the size of the class instantly"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Print in stdout the square by using #"""
        if self.__size > 0:
            for row in range(self.__size):
                for col in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
