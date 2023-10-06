#!/usr/bin/python3
"""class User inheirits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """handle user's information

    Attributes:
        email (str): user's email address
        password (str): email password
        first_name (str): user's first name
        last_name (str):: user's last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
