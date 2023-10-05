#!/usr/bin/python3
# base_model.py
"""Defines a new class BaseModel"""
from  uuid import uuid4
from datetime import datetime


class BaseModel:
    """Creates an new BaseModel"""

    def __init__(self):
        """Initializes a new instance of BaseModel"""
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        """Creates the string representation of the obj"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """Updates most recent change time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Creates a dictionary representation of the obj"""
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
