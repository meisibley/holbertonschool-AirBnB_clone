#!/usr/bin/python3
"""class amenity inherits from BaseModel"""
from models.base_model import BaseModel


def __init__(self, name=""):
    """attribute name is public

    arg:
        name: a string value
    """

    self.name = name
