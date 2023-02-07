#!/usr/bin/python3
"""Module to define a class named Student
"""


class Student:
    """A class named Student

    Attributes:
        first_name(str): the first name of the student
        last_name(str): the last name of the student
        age(int): the age of the student
    """

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of Student"""
        if (type(attrs) is list and
                all(type(element) is str for element in attrs)):
            dictionary = {}
            for i in attrs:
                if i in self.__dict__:
                    dictionary[i] = self.__dict__[i]
            return dictionary
        else:
            return self.__dict__
