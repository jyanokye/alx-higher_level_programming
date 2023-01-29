#!/usr/bin/python3
"""This module has the append after function"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each \
    line containing a specific string"""

    with open(filename, mode='r+', encoding='utf-8') as file_:
        lines = []
        while True:
            line = file_.readline()
            if line == '':
                break
            lines.append(line)
            if search_string in line:
                lines.append(new_string)

    with open(filename, mode='w', encoding='utf-8') as file_:
        file_.writelines(lines)
