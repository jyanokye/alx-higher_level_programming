#!/usr/bin/python3
"""A function that adds attributes to objects."""


def add_attribute(obj, name_of_att, value):
    """Add a new attribute to an object if possible.
    Args:
    obj (any): The object to add an attribute to.
    name_of_att (str): The name of the attribute to be added.
    value (any): The value of the attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name_of_att, value)
