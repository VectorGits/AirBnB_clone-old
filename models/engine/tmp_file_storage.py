#!/usr/bin/python3
"""
The FileStorage Module
"""

# import the json module for handling JSON data
import json

# import the os module for interacting with the os
import os


class FileStorage:
    """
    The FileStorage class is responsible for serializing instances
    to a JSON file and deserializing JSON files back to instances.
    It serves as a central storage mechanism for persisting and
    retrieving objects in the AirBnB console.

    Attributes:
    - __file_path (str): The default file path for storing JSON data.
    - __objects (dict): A dictionary to store serialized instances,
        with keys in the format '<class_name>.<instance_id>'.

    Methods:
    - all(self): Returns the dictionary __objects containing
        all stored instances.
    - new(self, obj): Adds a new object to __objects with a key
        derived from the object's class name and ID.
    - save(self): Serializes __objects to the JSON file specified
        by __file_path.
    - classes(self): Returns a dictionary mapping class names
        to their corresponding types.
    - reload(self): Deserializes the JSON file to __objects,
        only if the file exists.
    """

    # define the default file path for storing JSON data
    __file_path = "file.json"
    # initialize an empty dictionary to store serialized instances
    __objects = {}

    @property
    def file_path(self):
        """
        Getter method for the 'file_path' property.
        """

        return FileStorage.__file_path

    @property
    def objects(self):
        """
        Getter method for the 'objects' property.
        """

        return FileStorage.__objects

    def all(self):
        """
        Returns the dictionary __objects.
        """

        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the object with key <obj class name>.id.
        """

        # create a key using the object's class name and ID
        key = f"{type(obj).__name__}.{obj.id}"
        # add the object to the __objects dictionary with the generated key
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file specified by __file_path.
        """

        # create a new dictionary to store serialized objects
        serialized_objects = {}
        # iterate through each key-value pair in __objects
        for key, obj in self.__objects.items():
            # convert each object to a dictionary using its to_dict method
            serialized_objects[key] = obj.to_dict()

        # open the file specified by __file_path
        # and write the serialized_objects as JSON
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(serialized_objects, file)

    def classes(self):
        """
        Returns the dictionary mapping class names
        to their corresponding types.
        """
        # import the BaseModel class from the base_model module
        from models.base_model import BaseModel

        # add other classes as needed
        classes = {
            "BaseModel": BaseModel,
            # add other classes here as needed
        }
        return classes

    def reload(self):
        """
        Deserializes the JSON file to __objects only if the file exists.
        """

        # check if the JSON file exists
        if not os.path.isfile(self.__file_path):
            return

        try:
            # attempt to open the JSON file for reading
            with open(self.__file_path, "r", encoding="utf-8") as file:
                # load the JSON data into loaded_objects
                loaded_objects = json.load(file)

            # iterate through each key-value pair in loaded_objects
            for key, obj_dict in loaded_objects.items():
                # retrieve the class type from the classes dictionary
                class_type = self.classes()[obj_dict["__class__"]]

                # create an instance of the class using the provided dictionary
                obj_instance = class_type(**obj_dict)
                # add the object instance to __objects
                # with the corresponding key
                self.__objects[key] = obj_instance

        except json.JSONDecodeError as e:
            # handle potential issues with JSON decoding
            print(f"error decoding JSON: {e}")

        except FileNotFoundError:
            pass  # if the file doesn't exist, do nothing
