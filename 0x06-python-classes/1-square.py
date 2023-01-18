#!/usr/bin/python3
"""a class `Square` that defines a square by: (based on 0-square.py)
Private instance attribute: `size`
"""


class Square:
    """Defines a square"""

    def __init__(self, size):
        """ Initialises a new square

        Args:
        size (int): the size of the new square

        """

        self.__size = size
