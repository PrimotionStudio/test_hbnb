#!/usr/bin/env python3
"""
Module Containing User Class from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class representing a User object in the database
    """

    def __init__(self, email="", password="", first_name="",
                 last_name="", *args, **kwargs):
        """
        Initialize a new instance of the User class
        """
        super().__init__(*args, **kwargs)
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
