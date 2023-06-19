#!/usr/bin/python3

"""
module that contains the base class 'Base'
"""
from json import dumps, loads


class Base:
    """
    This class will be the “base” of all other classes in this project.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        '''Constructor.'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def load_from_file(cls):
        """creates a list of instances from a json file"""
        try:
            with open(cls.__name__ + ".json", "r") as file:
                lista = Base.from_json_string(file.read())
                return [cls.create(**dic) for dic in lista]
        except IOError:
            return []

    @classmethod
    def create(cls, **dictionary):
        """creates a new instance initialized by dictionary"""
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            new = Rectangle(5, 5)
        elif cls is Square:
            new = Square(5)
        else:
            new = None
        new.update(**dictionary)
        return new

    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None or json_string == '':
            return []
        return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON serialization of a list of objects to a file."""
        with open((cls.__name__ + ".json"), "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]\n")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts) + '\n')

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string of the objects in the list"""
        if list_dictionaries is None:
            return '[]'
        else:
            return dumps(list_dictionaries)
