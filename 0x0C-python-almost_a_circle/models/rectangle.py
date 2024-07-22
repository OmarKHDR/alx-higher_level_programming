from models.base import Base
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
        if type(val) is not int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = val
        return

    @property
    def height(self):
        """help"""
        return self.__height

    @height.setter
    def height(self, val):
        """find me"""
        if type(val) is not int:
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = val
        return

    @property
    def x(self):
        """someone stop this sh1t"""
        return self.__x

    @x.setter
    def x(self, val):
        """see me"""
        if type(val) is not int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = val
        return

    @property
    def y(self):
        """do you"""
        return self.__y

    @y.setter
    def y(self, val):
        """doyou """
        if type(val) is not int:
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = val
        return
