#!/usr/bin/python3
"""Creates class Square"""


class Square:
    """A class that defines a square by size"""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Getter: Return the size of an existing Square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter: Changes size of existing Square

        Args:
            value (int): The new size of the Square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates area of square returns: area"""
        return self.__size ** 2

    def my_print(self):
        """Prints a square based on self.__size"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
