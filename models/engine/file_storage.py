#!/usr/bin/python3
"""This module is used to serializes instances to a JSON file
and deserializes JSON file to instances"""
import json
from models.base_model import BaseModel


class FileStorage:
    """This is a class that serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
    __file_path (string) : the  path to the json file
     __objects (dictionary): the data structure
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This method returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """This method sets in __objects the obj with key
        <obj class name>.id"""
        class_name = obj.__class__.__name__
        obj_id = obj.id
        self.__objects[f"{class_name}.{obj_id}"] = obj

    def save(self):
        """The save method serializes __objects to the
        JSON file (path: __file_path)
        """
        # serializing the object to a dict and then use
        # json.dumps to serialise it to a json string
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        des_json = json.dumps(obj_dict)
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            f.write(des_json)

    def reload(self):
        """This method deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise,
        do nothing. If the file doesn't exist, no exception
        should be raised)
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                des_dict = json.load(f)
                self.__objects = des_dict
        except FileNotFoundError:
            pass
