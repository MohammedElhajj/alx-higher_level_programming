#!/usr/bin/python3
"""This module creates a class named Rectangle"""


class Rectangle:
    """A class named Rectangle

    AAttributes:
        width(int): the width of the rectangle
        height(int): the height of the rectangle
        number_of_instances(int): Rectangle instances number
        print_symbol(any): the symbol for string representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        """Return a representation of the rectangle using #"""
        rect = ""
        if self.__width == 0 or self.__height == 0:
            return (rect)
        for row in range(self.__height):
            for column in range(self.__width):
                rect += str(self.print_symbol)
            if row < self.__height - 1:
                rect += "\n"
        return (rect)

    def __repr__(self):
        """Return the string representation of the rectangle"""
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Return the biggest rectangle based on the area

        Args:
            rect_1(Rectangle): the first Rectangle
            rect_2(Rectangle): the second Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance with width & height == size"""
        return (cls(size, size))
