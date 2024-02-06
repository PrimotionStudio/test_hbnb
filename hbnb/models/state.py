#!/usr/bin/env python3
"""
Module Containing State Class from BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Class representing a State object in the database
    """

    def __init__(self, name="", *args, **kwargs):
        """
        Initialize a new instance of the State class
        """
        super().__init__(*args, **kwargs)
        self.name = name
