#!/usr/bin/python3
"""Module for Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class and the attributes"""
    place_id = ""
    user_id = ""
    text = ""
