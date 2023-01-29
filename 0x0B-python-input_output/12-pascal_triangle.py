#!/usr/bin/python3
"""This module contains the function pascal triangle()"""


def pascal_triangle(n):
    """ returns a list of lists of integers \
    representing the Pascal’s triangle of n
    Args:

    n (int): n whose pascal_triangle is to be printed
    """
    if n <= 0:
        return []

    triangle = [[1]]

    while len(triangle) != n:
        list_ = triangle[-1]
        item = [1]
        for i in range(len(list_) - 1):
            item.append(list_[i] + list_[i + 1])
        item.append(1)
        triangle.append(item)
    return triangle
