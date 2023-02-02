#!/usr/bin/python3
""" class Student"""


class Student:
    """a class that defines a student"""
    def __init__(self, first_name, last_name, age):
        """initializes the object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a \
        Student instance
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance
        Args:

        json (dict): Key/value pairs to replace attributes
        """
        for i, j in json.items():
            setattr(self, i, j)
