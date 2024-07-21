#!/usr/bin/python3
"""easy --==--"""


def write_file(filename="", text=""):
    """ reading
        args: filename
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
