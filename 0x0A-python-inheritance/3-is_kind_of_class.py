#!/usr/bin/python3
"""a function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """eturns True if the object is an instance of, or if the object \
    is an instance of a class that inherited from, the specified \
    class ; otherwise False
    """
    if type(obj) == a_class or isinstance(obj, a_class):
        return True
    else:
        return False
