#!/usr/bin/python3
"""module that contains Base class"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """INIT"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries:"""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save dict to json"""
        d = []
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            if list_objs:
                for obj in list_objs:
                    d.append(obj.to_dictionary())
            f.write(cls.to_json_string(d))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string:"""

        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set:"""

        if cls.__name__ == 'Rectangle':
            new = cls(1, 1)

        if cls.__name__ == 'Square':
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """returns a list of instances:"""
        try:
            with open(cls.__name__ + ".json", "r") as f:
                return [cls.create(**dictionary) for
                        dictionary in cls.from_json_string(f.read())]
        except FileNotFoundError:
            return []
