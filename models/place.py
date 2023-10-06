#!/usr/bin/python3
"""class Place inherits from BaseModel"""
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.amenity import Amenity


def __init__(self, name="", description="", number_rooms=0, number_bathrooms=0,
             max_guest=0, price_by_night=0, latitude=0.0, longitude=0.0):
    """place information include city, user and amenity attributes

    args:
        name: a string
        description: a string
        number_rooms: an integer, how many rooms in the house
        number_bathrooms: an integer, how many bathrooms in the house
        max_guest: an integer, how many guests house can hold
        price_by_night: an integer
        latitude: a float value
        longitude: a float value
    """

    self.city_id = City.id
    self.user_id = User.id
    self.name = name
    self.description = description
    self.number_rooms = number_rooms
    self.number_bathrooms = number_bathrooms
    self.max_guest = max_guest
    self.price_by_night = price_by_night
    self.latitude = latitude
    self.longitude = longitude
    self.amenity_ids = Amenity.id
