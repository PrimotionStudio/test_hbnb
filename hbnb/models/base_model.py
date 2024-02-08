#!/usr/bin/python3
"""
    Base Model of the hbnb console
"""
import cmd
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel(cmd.Cmd):
    """
    This is a base class for handling commands in the HBNB Console
    """

    inst = 0

    def __init__(self, *args, **kwargs):
        """
        Constructor for initializing the BaseModel object
        :param args: Arguments passed to the constructor
        :param kwargs: Keyword arguments passed to the constructor
        """
        if kwargs:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k in ["created_at", "updated_at"]:
                        setattr(self, k, datetime.strptime(
                            v, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
            BaseModel.inst += 1

    def __str__(self):
        """
        Returns a string representation of an instance of the BaseModel class
        :return: A string representing the instance of the BaseModel class
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """
        Saves the current instance of the model into the database
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Convert this object to a dictionary (for json serialization)
        """
        return {"__class__": self.__class__.__name__,
                **{k: v.isoformat()
                   if k in ["created_at", "updated_at"]
                   else v for k, v in self.__dict__.items()}}
