#!/usr/bin/python3
"""Define class Base"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries:
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries, skipkeys=True)
