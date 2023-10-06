#!/usr/bin/python3
"""class City inherit from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """Defines new class City

    Attributes:
        state_id (str): The State id
        name (str): city name
    """
    state_id = ""
    name = ""
