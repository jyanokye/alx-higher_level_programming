#!/usr/bin/python3
""" defines a class, BaseGeometry"""


class BaseGeometry:
    """A class"""
    def __init__(self):
        """Initialises the object"""

    def area(self):
        """raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if not isinstance(value, int) or type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
