#!/usr/bin/python3
"""The class defines a city."""
from models.base_model import BaseModel


class City(BaseModel):
    """this defines a city.

    Attributes:
        state_id (str): This is the state id.
        name (str): This is the name of the city.
    """

    state_id = ""
    name = ""
