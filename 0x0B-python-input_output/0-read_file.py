#!/usr/bin/python3
"""easy --==--"""


def read_file(filename=""):
    """ reading
        args: filename
    """
    with open(filename, 'r') as f:
        line = f.readline()
        while len(line) > 0:
            print(line, end='')
            line = f.readline()
