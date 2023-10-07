#!/usr/bin/python3
"""class amenity inherits from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines new class Amenity

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
