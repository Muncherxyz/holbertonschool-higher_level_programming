#!/usr/bin/python3
"""Created class Square"""


class Square:
    """Square class with size and position attributes"""

    def __init__(self, size=0, position=(0, 0)):
        """Creates a Square with size and position"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter: Returns the size of an existing Square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter: Alters the size of an exisiting Square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter: Gets the position of the Square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter: Sets the position of the Square"""
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(num, int) for num in value) or \
           any(num < 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Compute and return the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Print the square with # character"""
        if self.__size == 0:
            print()
            return
        [print() for i in range(self.__position[1])]
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
