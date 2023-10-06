#!/usr/bin/python3
"""class User inheirits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """handle user's information

    arg:
        email: user's email address
        password: email password
        first_name: user's first name
        last_name: user's last name
    """

    def __init__(self, email="", password="", first_name="", last_name=""):
        """all attributes are public"""
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
