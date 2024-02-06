#!/usr/bin/python3
"""
Module Containing Review Class from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class representing a Review object in the database
    """

    def __init__(self, place_id="", user_id="", text="", *args, **kwargs):
        """
        Initialize a new instance of the Review class
        """
        super().__init__(*args, **kwargs)
        self.place_id = place_id
        self.user_id = user_id
        self.text = text
