#!/usr/bin/python3
"""class City inherit from BaseModel"""
from models.base_model import BaseModel
from models.state import State


def __init__(self, name=""):
    """all attributes are public

    arg:
        name: city name
    """

    self.state_id = State.id
    self.name = name
