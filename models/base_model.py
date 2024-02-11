#!/usr/bin/python3
"""
The BaseModel Module
"""

# import the 'uuid' module to generate universally unique identifiers (UUIDs)
import uuid

# import the datetime class from the datetime mod for working with timestamps
from datetime import datetime


class BaseModel:
    """
    BaseModel class serves as a base class for other classes in the project.

    Public instance attributes:
    - id:
        string - Universally Unique Identifier (UUID) assigned
        when an instance is created.
    - created_at:
        datetime - Timestamp of when an instance is created.
    - updated_at:
        datetime - Timestamp updated every time the object is modified.

    Public instance methods:
    - __str__(): Returns a string representation of the instance.
    - save(): Updates the 'updated_at' attribute with the current datetime.
    - to_dict(): Returns a dictionary representation of the instance,
    suitable for serialization.
    """

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of the BaseModel class."""

        # default attribute assignments when no kwargs are provided
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        # initialize class_name to None,
        # it will be used to store the class name extracted from kwargs
        class_name = None

        # check if kwargs are provided during instantiation
        if kwargs:
            # use 'pop()' to retrieve and remove the value associated with the
            # __class__ key from the kwargs dictionary if it exists, if the
            # key is not found, assign the default value None to 'class_name'
            class_name = kwargs.pop("__class__", None)

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
                    setattr(self, key, value)

        # if __class__ was provided, instantiate the correct class
        if class_name:
            # use globals() to retrieve the global namespace as a dictionary
            # and then get the class object associated with the class_name
            class_ = globals().get(class_name)

            # check if class_ is not None and is a subclass of BaseModel
            if class_ and issubclass(class_, BaseModel):
                # set the instance's class to the retrieved class_
                self.__class__ = class_

    def __str__(self):
        """String representation of an instance."""
        # return a formatted string containing class name, id, and attributes
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the 'updated_at with the current datetime."""

        # set 'updated_at' attribute to the current date and time
        self.updated_at = datetime.now()

    def to_dict(self):
        """Dictionary representation of an instance."""

        # create a copy of the instance's attribute dictionary
        # to avoid modifying the original
        instance_dict = self.__dict__.copy()

        # remove the '__class__' key if present, to ensures a fresh start,
        # preventing conflicts with any pre-existing __class__ key in the dict
        # instance_dict.pop("__class__", None)

        # add a key '__class__' with the name of the instance's class
        # to ensure that the '__class__' key reflects the current class
        instance_dict["__class__"] = type(self).__name__

        # convert 'created_at' and 'updated_at' attributes
        # to ISO format strings
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()

        # instance_dict.pop("__class__", None)

        # return the modified dictionary
        return instance_dict
