#!/usr/bin/python3
"""This Module creates a new, empty class called Square."""


class Square:
    """Class that defines a square by size"""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0."""
        self.size = size

    @property
    def size(self):
        """Getter: Returns size of existing Square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter: Alters size of existing square

        Args:
            value (int): New size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0."""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Return the current square area"""
        return self.__size ** 2
