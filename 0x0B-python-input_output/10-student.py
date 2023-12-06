#!/usr/bin/python3
"""
    Module for class Student
"""


class Student:
    """
        A class students that defines a student by:
        Attributes:
            first_name : name of student.
            last_name : name of student.
            age : age of student.
        Methods:
            __init__ - initializes the Student instance.
            to_json - retrieves dictionary repr of Student instance.
    """
    def __init__(self, first_name, last_name, age):
        """
            Initialises Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """
            retrieves a dictionary representation of Student.
            Args:
                attr : attribute names that are to be retrieved.
        """

        if attr is not None:
            reslt = {at: self.__dict__[at]
                     for at in self.__dict__.keys() & attr}
            return reslt
        else:
            return self.__dict__
