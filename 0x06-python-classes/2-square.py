#!/usr/bin/python3
"""Making a new class called Square"""


class Square:
    """THe SUMmary summary    """
    def __init__(self, size=0) -> None:
        """THe SUMmary summary

        Args:
            size = 0
        """
        if type(size) is not int:
            raise TypeError("size must be integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
