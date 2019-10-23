#!/usr/bin/python3
"""
defines the class square, who inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class that inherits from Rectangle. It defines a Square

    Attributes:
        __x (int): x position
        __y (int): y position
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Init method for class. It calls the super function to initialize
        Rectangle

        The width and height must be assigned to the value of size

        All width, height, x and y validation inherit from Rectangle
        - same behavior in case of wrong data

        Args:
            size (int): width and height of square
            x (int): x position of square
            y (int): y position of square
            id (int): id of square
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Printable form of class
        """

        args = (self.id, self.x, self.y, self.width)
        return '[Square] ({}) {}/{} - {}'.format(*args)

    @property
    """
    getter for size
    Returns thee width of Rectangle

    setter validates same as Rectangle's attributes
    setter
    sets width and height
    """
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError('width must be an integer')
        if size <= 0:
            raise ValueError('width must be > 0')
        self.width = size
        self.height = size
