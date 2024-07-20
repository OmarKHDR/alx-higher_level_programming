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
    for i in range(counter):
        print("BestSchool", end=("", ", ")[i < counter - 1])
    return ""
