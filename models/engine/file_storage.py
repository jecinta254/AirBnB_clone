#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Representation of abstracted storage engine.

    P. Attributes:
        __file_path (str): The name of file to save objects to.
        __objects (dict): A dictionary of instance objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        obj_class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_class_name, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        od = FileStorage.__objects
        objd = {obj: od[obj].to_dict() for obj in od.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objd, f)

    def reload(self):
        """Deserial the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objd = json.load(f)
                for item in objd.values():
                    ourclass = item["__class__"]
                    del item["__class__"]
                    self.new(eval(ourclass)(**item))
        except FileNotFoundError:
            return
