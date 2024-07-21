#!/usr/bin/python3
"""file append"""


def append_write(filename="", text=""):
    """ file append fowawa"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
