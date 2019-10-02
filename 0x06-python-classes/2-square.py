#!/usr/bin/python3
""" Write a class Square that defines a square """


class Square():
    """ Defines a Square.

    Attrinutes:
        __size (int): Size of square.

    """

    def __init__(self, size=0):
        """ Assign attributes with the args passed

        Args:
            size (int): size of square

        """
        if not isinstance(size, int):
            raise TypeError("Size must be and integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
