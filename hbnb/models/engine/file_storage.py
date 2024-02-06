#!/usr/bin/python3
"""
a Module file_storage that serializes instances to a JSON
file and deserializes JSON file to instances
"""
import json
from datetime import datetime
from pprint import pprint


class FileStorage:
    """
    A class that provides methods for saving objects as JSON files,
    loading them from such files, and getting the list of saved items.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns a dictionary with all saved objects in format {id : object}
        """
        return (self.__class__.__objects)

    def new(self, obj):
        """
        Saves an object into a JSON file.
        If the object already exists - updates it.
        The id is generated automatically based on current time.
        """
        self.__class__.__objects["<{}>.{}".format(
            obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        Serializes all saved objects into a JSON file.
        """
        new_dict = {}
        for k, v in self.__class__.__objects.items():
            """ v.to_dict() also converts the dates and time to isoformat """
            new_dict[v.__class__.__name__+"."+v.id] = v.to_dict()
        with open(self.__class__.__file_path, "w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """
        Loads saved objects from the JSON file if one exists.
        """
        try:
            from models.base_model import BaseModel
            from models.user import User
            from models.amenity import Amenity
            from models.city import City
            from models.place import Place
            from models.review import Review
            from models.state import State

            with open(self.__class__.__file_path, "r") as f:
                line = f.read()
                obj_dict = {k: v for k, v in json.loads(line).items()}
                for j in obj_dict.values():
                    try:
                        new_bm = locals()[j["__class__"]](**j)
                        self.new(new_bm)
                    except KeyError:
                        pass

        except FileNotFoundError as fnfe:
            pass
