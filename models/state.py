#!/usr/bin/python3
"""class State inherit from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """class State represents state

    args:
        name: string
    """

    def __init__(self, name=""):
        """name is a public attribute"""
        self.name = name
