from base import Base
"""fuel"""


class Rectangle(Base):
    """yes it is my tenth rect class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """normal init with args we dont need"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """pro"""
        return self.__width

    @width.setter
    def width(self, val):
        """pls"""
        self.__width = val
        return

    @property
    def height(self):
        """help"""
        return self.__height

    @height.setter
    def height(self, val):
        """find me"""
        self.__height = val
        return

    @property
    def x(self):
        """someone stop this sh1t"""
        return self.__x

    @x.setter
    def x(self, val):
        """see me"""
        self.__x = val
        return

    @property
    def y(self):
        """do you"""
        return self.__y

    @y.setter
    def y(self, val):
        """doyou """
        self.__y = val
        return
