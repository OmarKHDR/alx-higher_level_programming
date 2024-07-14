#!/usr/bin/python3

class Rectangle:
    def __init__(self, width=0, height=0) -> None:
        self.width = width
        self.height = height
    
    @property
    def width(self):
        return self.width
    
    @width.setter
    def width(self, width):
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(width) is not int:
            raise TypeError("width must be integer")
        self.width = width

    @property
    def height(self):
        return self.height
    
    @height.setter
    def width(self, height):
        if height < 0:
            raise ValueError("height must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be integer")
        else:
            self.height = height

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)
