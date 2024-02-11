#!/usr/bin/python3
"""Defines the Place described in the class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represent a place.

    Attributes:
        city_id (str): The City id.
        user_id (str): The User id.
        name (str): The name given to the place.
        description (str): This is the place's description.
        number_rooms (int): The number of rooms of the place.
        number_bathrooms (int): The number of bathrooms in the place
        max_guest (int): The maximum number of guests of the place.
        price_by_night (int): This is price aby night
        latitude (float): The latitude of the place
        longitude (float): This is the longitude of the place.
        amenity_ids (list): An empty list of Amenity ids.
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
