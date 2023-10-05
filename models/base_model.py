#!/usr/bin/python3
# base_model.py
"""Defines a new class BaseModel"""
import UUID
import datetime

class BaseModel:
    """Creates an new BaseModel"""

    def __init__(self):
        """Initializes a new instance of BaseModel"""
        id = str(uuid.uuid4())
        created_at = datetime.datetime.now()
        updated_at = datetime.datetime.now()

    def __str__(self):
        """Creates the string representation of the obj"""
        return ("[{}] ({}) {}".format(self.__name__, self.id, self.__dict__))

    def save(self):
        """Updates most recent change time"""
        updated_at = datetime.datetime.now()

    def to_dict(self):
        """Creates a dictionary representation of the obj"""
        return {
                "__class__": self.__name__,
                "id": self.__dict__,
                "created_at": self.created_at.isoformat(),
                "updated_at": self.updated_at.isoformat()
                }
