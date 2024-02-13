#!/usr/bin/python3
"""
The BaseModel Module
"""

# import the 'uuid' module to generate universally unique identifiers (UUIDs)
import uuid

# import the datetime class from the datetime mod for working with timestamps
from datetime import datetime

# import the storage module from the models package
from models import storage


class BaseModel:
    """
    BaseModel class serves as a base class for other classes in the project.

    Attributes:
    - id:
        string - Universally Unique Identifier (UUID) assigned
        when an instance is created.
    - created_at:
        datetime - Timestamp of when an instance is created.
    - updated_at:
        datetime - Timestamp updated every time the object is modified.

    Methods:
    - __init__(*args, **kwargs): Initializes a new instance of
        the BaseModel class.
        If kwargs are provided, sets attributes based on the key-value pairs.
    - __str__(): Returns a string representation of the instance.
    - save(): Updates the 'updated_at' attribute with the current datetime
        and saves the instance.
    - to_dict(): Returns a dictionary representation of the instance,
        suitable for serialization.
    """

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of the BaseModel class."""

        # default attribute assignments when no kwargs are provided
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        # check if kwargs are provided during instantiation
        if kwargs:
            # iterate through key-value pairs in kwargs
            for key, value in kwargs.items():
                # check if the key is "created_at" or "updated_at"
                if key == "created_at" or key == "updated_at":
                    # parse and set datetime attributes
                    # based on the provided value
                    setattr(
                        self,
                        key,
                        datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"),
                    )
                else:
                    # set regular attribute based
                    # on the provided key-value pair
                    self.__dict__[key] = value

        # check if no kwargs are provided during instantiation
        if not kwargs:
            # add the current instance to the storage
            storage.new(self)

    def __str__(self):
        """String representation of an instance."""

        # return a formatted string containing class name, id, and attributes
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the 'updated_at with the current datetime."""

        # set 'updated_at' attribute to the current date and time
        self.updated_at = datetime.now()

        # save the changes to the storage
        storage.save()

    def to_dict(self):
        """Dictionary representation of an instance."""

        # create a copy of the instance's attribute dictionary
        # to avoid modifying the original
        instance_dict = self.__dict__.copy()

        # add a key '__class__' with the name of the instance's class
        # to ensure that the '__class__' key reflects the current class
        instance_dict["__class__"] = type(self).__name__

        # convert 'created_at' and 'updated_at' attributes
        # to ISO format strings
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()

        # return the modified dictionary
        return instance_dict
