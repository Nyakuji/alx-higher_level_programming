#!/usr/bin/python3
""" Module Square """


class Square:
    """ Square class defined by (based on 1-square.py)

        Attributes: (private)
            size (int): Size of square
    """
    def __init__(self, size=0):
        """
        Initialize method

        Args:
            size (int): int to assign to optional square size
        Raises:
            TypeError: if size is not int
            ValueError: size less than 0
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
