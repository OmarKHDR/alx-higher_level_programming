#!/usr/bin/python3

class Rectangle:
    number_of_instances = 0
    print_symbol = '#'
    def __init__(self, width=0, height=0) -> None:
        Rectangle.number_of_instances += 1
        self.__width = width
        self.__height = height
    
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, width):
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(width) is not int:
            raise TypeError("width must be integer")
        self.__width = width

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, height):
        if height < 0:
            raise ValueError("height must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be integer")
        else:
            self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            length = 2 * (self.__width + self.__height)
            return length

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        shape = (Rectangle.print_symbol * self.__width +"\n") * self.__height
        return shape.rstrip('\n')

            
    def __repr__(self):
        return f"Rectangle({self.__width},{self.__height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
    
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1,Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area >= rect_2.area:
            return rect_1
        else :
            return rect_2


