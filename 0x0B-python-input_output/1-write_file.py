#!/usr/bin/python3
"""This module has a function for writing to a file"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and returns \
    the number of characters written
    """
    with open(filename, mode='w', encoding='utf-8') as file_:
        n_char = file_.write(text)
        return n_char
