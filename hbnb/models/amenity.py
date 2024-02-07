#!/usr/bin/python3
"""
Author : karyna <karyna@localhost>
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity Class that inheritrs from BaseModel
    """

    inst = 0
    def __init__(self, name="", *args, **kwargs):
        """
        Initialize a new instance of the Amenity class.
        """
        super().__init__(*args, **kwargs)
        self.name = name
        Amenity.inst += 1
