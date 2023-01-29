#!/usr/bin/python3
"""This module has a function that appends text to a file"""


def append_write(filename="", text=""):
    """appends text to file

    Args:
    filename (str): name of the file
    text (str): text to be appended
    """
    with open(filename, mode='a', encoding='utf-8') as file_:
        n_char = file_.write(text)
        return n_char
