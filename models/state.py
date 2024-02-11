#!/usr/bin/python3
"""Defines the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """ The class defines a state.

    Attributes:
        name (str): This is the name of the state.
    """

    name = ""
