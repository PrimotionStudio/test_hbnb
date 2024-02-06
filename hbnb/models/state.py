#!/usr/bin/python3
"""
Module Containing State Class from BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Class representing a State object in the database
    """

    __inst = 0

    def __init__(self, name="", *args, **kwargs):
        """
        Initialize a new instance of the State class
        """
        State.__inst += 1
        super().__init__(*args, **kwargs)
        self.name = name
