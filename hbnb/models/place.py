#!/usr/bin/python3
"""
Module containing a Place class thet inherits from a BaseModel
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Class representing a Place object in the database
    """
    inst = 0

    def __init__(self, city_id="", user_id="", name="", description="",
                 number_rooms=0, number_bathrooms=0, max_guest=0,
                 price_by_night=0, latitude=0.0, longitude=0.0, amenity_ids=[],
                 *args, **kwargs):
        """
        Initialize a new instance of the Place class
        """
        super().__init__(*args, **kwargs)
        self.city_id = city_id
        self.user_id = user_id
        self.name = name
        self.description = description
        self.number_rooms = number_rooms
        self.number_bathrooms = number_bathrooms
        self.max_guest = max_guest
        self.price_by_night = price_by_night
        self.latitude = latitude
        self.longitude = longitude
        self.amenity_ids = amenity_ids
        Place.inst += 1
