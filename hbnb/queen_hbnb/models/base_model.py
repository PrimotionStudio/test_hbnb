#!/usr/bin/python3
"""Module for the BaseModel class"""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel class that defines all common attributes/methods
    for other classes"""

    def __init__(self, *args, **kwargs):
        """Constructor for BaseModel class

        Args:
            *args: Unused variable length argument list
            **kwargs: Arbitrary keyword arguments
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        value = datetime.strptime(value,
                                                  "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns string representation of Basemodel instance

        Returns:
            str: String representation
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Update the public instance attribute 'updated_at'
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save(self)

    def to_dict(self):
        """Return a dictionary containing all keys/values
        of __dict__ of the instance
        """
        dict_instance = self.__dict__.copy()
        dict_instance["__class__"] = self.__class__.__name__
        dict_instance["created_at"] = self.created_at.isoformat()
        dict_instance["updated_at"] = self.updated_at.isoformat()
        return dict_instance
