#!/usr/bin/python3
"""Define class Base"""


class Base:
    """
    This class is the “base” of all other
    classes in this project. The goal of it is to manage
    id attribute in all your future classes

    Attributes:
        __nb_objects (int): number of instances
        id (int): id of instance. id if arg passed, __nb_obj otherwise
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Init method for class

        Args:
            id (int): id of instance. It's never the same
        """
        if not id:
            Base.__nb_objects += 1
            id = Base.__nb_objects
        self.id = id
