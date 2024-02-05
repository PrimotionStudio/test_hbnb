#!/usr/bin/env python3
"""
blah blah blah
"""
from models.base_model import BaseModel

class City(BaseModel):

    def __init__(self, name="", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
