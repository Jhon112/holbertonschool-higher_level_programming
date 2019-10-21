from .base import Base
"""Defines class Rectangle who inherits from Base class"""


class Rectangle(Base):
    """
    Class that inherits from base. It defines a Rectangle

    Attributes:
        __width (int): width of rectangle
        __height (int): height of rectangle
        __x (int): x position
        __y (int): y position
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Init for rectangle class. It initializes the super class(base)
        with id so the Base class manage it

        Args:
            width (id): width value of attr
            height (id): height value of attr
            x (id): x value of attr
            y (id): y value of attr
            id (int): id to be passed to super class
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y
