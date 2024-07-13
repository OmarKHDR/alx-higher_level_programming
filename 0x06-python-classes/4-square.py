#!/usr/bin/python3
"""Making a new class called Square"""


class Square:
    """THe SUMmary summary    """
    def __init__(self, size=0) -> None:
        """THe SUMmary summary

        Args:
            self
            size = 0
        """
        self.size = size

    @property
    def size(self):
        """THe SUMmary summary

        Args:
            self
        """
        return self._size

    @size.setter
    def size(self, s):
        """THe SUMmary summary

        Args:
            self
            s = 0
        """
        if type(s) is not int:
            raise TypeError("size must be integer")
        if s < 0:
            raise ValueError("size must be >= 0")

        self._size = s

    def area(self):
        """THe SUMmary summary

        Args:
            self
        """
        return self._size ** 2
