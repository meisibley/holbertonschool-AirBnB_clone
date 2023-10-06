#!/usr/bin/python3
"""class Review inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Defines new class Review

    Attributes:
        place_id (str): The place id.
        user_id (str): The user id.
        text (str): The text of the review
    """
    place_id = ""
    user_id = ""
    text = ""
