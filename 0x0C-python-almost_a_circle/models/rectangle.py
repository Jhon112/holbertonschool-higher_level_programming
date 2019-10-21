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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Setters and getters for all attributes
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            Rectangle.raise_typeError('width')
        elif width <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            Rectangle.raise_typeError('height')
        elif height <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            Rectangle.raise_typeError('x')
        elif x < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            Rectangle.raise_typeError('y')
        elif y < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = y

    # static methods
    @staticmethod
    def raise_typeError(attribute):
        """
        Method to raise TypeError when value is not
        instance of int.

        Args:
            attribute (str): attribute that couldn't be set
        """
        
        raise TypeError('{} must be an integer'.format(attribute))
