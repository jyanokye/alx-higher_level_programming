#!/usr/bin/python3
"""describes a class Square that is a subclass of class  Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
      """A subclass of rectangle"""
    def __init__(self, size):
        """ initializes the object

        Args:
        size (int): size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
