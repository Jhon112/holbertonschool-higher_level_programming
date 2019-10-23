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

        Args:
            list_dictionaries (list): list of dictionaries to convert

        return:
            json representation of list_dictionaries
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries, skipkeys=True, indent=2)

    @staticmethod
    def from_json_string(json_string):
        """
        gets the python list of the JSON string representation json_string

        Args:
            json_string (json): JSON representation of a list with all
                                the dictionaries

        return:
            (obj): python obj of JSON string
        """

        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string, encoding="utf-8")

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file:

        list_objs is a list of instances who inherits of Base

        If list_objs is None, save an empty list

        The filename must be: <Class name>.json

        use the static method to_json_string (created before)

        overwrite the file if it already exists
        """

        with open("{}.json".format(cls.__name__), mode="w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                json_list_dicts = Base.to_json_string(list_dicts)
                file.write(json_list_dicts)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes on dictionary already set

        Args:
            dictionary(dict): dictionary with attributes to be set

        Return:
            (obj): instance with all attributes set
        """

        # create dummy instance to call update
        instance = cls(5, 5)

        # update instance attributes with update method
        instance.update(**dictionary)

        return instance


