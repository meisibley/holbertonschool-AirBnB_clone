#!/usr/bin/python3
"""class Review inherits from BaseModel"""
from models.base_model import BaseModel
from models.place import Place
from models.user import User


class Review(BaseModel):
    """Defines new class Review"""

    def __init__(self, text=""):
        """attribute text is a string

        arg:
            text: string
        """
        self.place_id = Place.id
        self.user_id = User.id
        self.text = text
