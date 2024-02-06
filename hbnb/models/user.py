#!/usr/bin/python3
"""
Module Containing User Class from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class representing a User object in the database
    """

    __inst = 0

    def __init__(self, email="", password="", first_name="",
                 last_name="", *args, **kwargs):
        """
        Initialize a new instance of the User class
        """
        User.__inst += 1
        super().__init__(*args, **kwargs)
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
