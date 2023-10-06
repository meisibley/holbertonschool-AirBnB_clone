#!/usr/bin/python3
"""class amenity inherits from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines new class Amenity"""

    def __init__(self, name=""):
        """attribute name is public

        arg:
            name: a string value
        """
        self.name = name
