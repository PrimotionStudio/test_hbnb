#!/usr/bin/env python3
"""
    Base Model of the hbnb console
"""
import cmd
from uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel(cmd.Cmd):
    """
    docstring for BaseModel
    """

    def __init__(self, *args, **kwargs):
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

    def __str__(self):
        return ("[{}] ({}) <{}>".format(self.__class__.__name__,
                                        self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        return {"__class__": self.__class__.__name__,
                **{k: v.isoformat()
                   if k in ["created_at", "updated_at"]
                   else v for k, v in self.__dict__.items()}}
