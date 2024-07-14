#!/usr/bin/python3
"""Making a new class called Square"""


class Square:
    """THe SUMmary summary    """
    def __init__(self, size=0, pos=(0, 0)) -> None:
        """THe SUMmary summary

        Args:
            self
            size = 0
        """
        self.size = size
        self.__position = pos

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

    @property
    def position(self):
        """THe SUMmary summary

        Args:
            self
        """
        return self.__position

    @position.setter
    def position(self, pos):
        """THe SUMmary summary

        Args:
            self
        """
        if isinstance(pos, tuple) and len(pos) == 2 \
            and isinstance(pos[0], int) and isinstance(pos[1], int) \
                and pos[0] >= 0 and pos[1] >= 0:
            self.__position = pos
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """THe SUMmary summary

        Args:
            self
        """
        return self._size ** 2

    def my_print(self):
        """THe SUMmary summary

        Args:
            self
        """
        if self._size == 0:
            print()
            return
        print("\n" * self.__position[1], end="")
        for i in range(self._size):
            print(" " * self.__position[0] + "#" * self._size)

    def __str__(self) -> str:
        name = ""
        if self._size == 0:
            name+="\n"
        name += "\n" * self.__position[1] + (" " * self.__position[0] + "#" * self._size +"\n") * self._size
        return name

