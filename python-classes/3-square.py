#!/usr/bin/python3
"""This Module creates a new, empty class called Square."""


class Square:
    """class Square Def"""
    def __init__(self, size=0,):
        
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size <  0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
            """
            calculates area of square
            returns: area

            """
            return self.__size ** 2
