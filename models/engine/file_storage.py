#!/usr/bin/python3
# file_storage.py
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Creates a kind of storage engine

    Attributes:
        __file_path (str): Where to save data
        __objects (dict): Empty - used to store objects by cls.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary stored in __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds obj to __objects using cls.id method"""
        ob_class = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ob_class, obj.id)] = obj

    def save(self):
        """Converts __objects to JSON file in __file_path."""
        obj_d = FileStorage.__objects
        ready_obj_d = {obj: obj_d[obj].to_dict() for obj in obj_d.keys()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(ready_obj_d, file)

    def reload(self):
        """If file exists add objects in file to __objects"""
        try:
            with open(FileStorage.__file_path) as file:
                obj_d = json.load(file)
                for obj in obj_d.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except IOError:
            pass
