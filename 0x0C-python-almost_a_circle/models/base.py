#!/usr/bin/python3
"""Define class Base"""


class Base:
    """
    This class will be the “base” of all other
    classes in this project. The goal of it is to manage
    id attribute in all your future classes

    Attributes:
        __nb_objects (int): number of instances
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if not id:
            Base.__nb_objects += 1
            id = Base.__nb_objects
        self.id = id
