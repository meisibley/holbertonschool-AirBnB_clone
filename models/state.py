#!/usr/bin/python3
"""class State inherit from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """Creates the class State

    Attributes:
        name (str): The name of the state
    """
    name = ""
