#!/usr/bin/python3
"""class Place inherits from BaseModel"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Defines a newclass Place

    Atributes:
        city_id (str): The city id
        user_id (str): User id
        name (str): The name of the place
        description (str): Describes the place
        number_rooms (int): Number of rooms
        number_bathrooms (int): The number of bathrooms
        max_guest (int): The maximum guests allowed
        price_by_night (int): The price by night
        latitude (float): The latitude of the location
        longitude (float): The longitude of the location
        amenity_ids (list): A list of Amenity ids
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
