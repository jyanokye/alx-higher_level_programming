#!/usr/bin/python3
"""initialize"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square"""

    def __init__(self, size):
        """first attributes"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
        self.area()
