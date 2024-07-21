#!/usr/bin/python3

""" file is not alright and and so am i"""


class BaseGeometry:
    """classes
    """
    def area(self):
        """ area
            args:
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ valid
            args : name, value
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ Rect"""

    def __init__(self, width, height):
        """ initialization
            args:
            width: and
            height:
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ area is mul """
        return self.__width * self.__height

    def __str__(self) -> str:
        """printing what you said"""
        return f"[{type(self).__name__}] {self.__width}/{self.__height}"


class Square(Rectangle):
    """square"""

    def __init__(self, size):
        """yeah boy"""
        super().__init__(size, size)
        self.__size = size
