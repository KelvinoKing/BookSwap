#!/usr/bin/python3
"""This is the file storage class for BookSwap"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.book import Book


class FileStorage:
    """This class will manage storage of BookSwap instances"""
    __file_path = "file.json"
    __objects = {}


    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                new_dict = json.load(f)
            for key, value in new_dict.items():
                FileStorage.__objects[key] = eval(value['__class__'])(**value)