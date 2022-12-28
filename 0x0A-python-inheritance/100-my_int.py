#!/usr/bin/python3
"""a class integer that inherits from int"""


class MyInt(int):
    """subclass of class int
    inverts int operators == and !=."""

    def __eq__(self, value):
        """Inverts == operator to !="""
        return self.real != value

    def __ne__(self, value):
        """Inverts != operator to =="""
        return self.real == value
