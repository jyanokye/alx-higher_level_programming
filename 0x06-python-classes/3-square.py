#!/usr/bin/python3
"""defining a square"""


class Square:
    """ represents a square

    Attributes:
        ___size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """Initializes square
        Args:
            size (int): size of a side of the square
        Returns: None
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

     def area(self):
        """calculates square's area

        Returns: None
        """
        return self.__size * self.__size
