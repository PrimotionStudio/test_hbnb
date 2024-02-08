#!/usr/bin/python3
"""
Module containing the City class that inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Class representing a city object in the database
    """
    inst = 0

    def __init__(self, state_id="", name="", *args, **kwargs):
        """
        Initialize a new instance of the City class
        Args:
            state_id (str): The ID of the State this City belongs to
            name (str): The name of the City
        """
        super().__init__(*args, **kwargs)
        self.state_id = state_id
        self.name = name
        City.inst += 1
