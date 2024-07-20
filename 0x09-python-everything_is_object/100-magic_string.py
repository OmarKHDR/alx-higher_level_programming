#!/usr/bin/python3

counter = 0


def magic_string():
    """
        arg:
        None,
        return empty string
    """
    global counter
    counter += 1
    print("BestSchool, " * (counter - 1) + "BestSchool", end="")
    return ""
