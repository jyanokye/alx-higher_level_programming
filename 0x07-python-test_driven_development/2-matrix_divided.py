#!/usr/bin/python3
""" divides all elements of a matrices. """


def matrix_divided(matrix, div):
    """divide all elements of a matrix"""
    core = 0
    if not all(isinstance(item, list) for item in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for thing in matrix:
        if not all(isinstance(obj, (int, float)) for obj in thing):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if len(matrix[0]) != len(row):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for member in matrix:
        new_mem = [round(p/div, 2) for p in member]
        new_matrix.append(new_mem)

    return new_matrix
