#!/usr/bin/python3
"""file.py"""


class Base:
    """my class"""
    __nb_objects = 0

    def __init__(self, id=None) -> None:
        """yeah oop"""
        if id == None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
