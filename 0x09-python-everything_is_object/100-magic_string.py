#!/usr/bin/python3
""" this file is no good"""
counter = 0


def magic_string():
    """ class of strings
        arg:
        None,
        return empty string
    """
    global counter
    counter += 1
    print("BestSchool, " * (counter - 1) + "BestSchool", end="")
    return ""
