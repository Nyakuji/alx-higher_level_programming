#!/usr/bin/python3
"""
A Student class that defines a Student (module)
"""


class Student():
    """
        a class Student that defines a student by: (based on 10-student.py)
    """
    def __init__(self, first_name, last_name, age):
        """
            Initialization
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            retrieves a dictionary representation
            of a Student instance
        """
        if type(attrs) is list and all([type(x) == str for x in attrs]):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return (self.__dict__)

    def reload_from_json(self, json):
        """
             replaces all attributes of the Student instance
        """
        for i, j in json.items():
            self.__dict__[i] = j
