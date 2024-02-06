#!/usr/bin/env python3
"""
blah blah blah
"""
from models.base_model import BaseModel


class Review(BaseModel):

    def __init__(self, place_id="", user_id="", text="", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.place_id = place_id
        self.user_id = user_id
        self.text = text
