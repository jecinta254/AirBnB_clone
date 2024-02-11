#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User.

    Public Attributes:
        email (str): This is the email of the user.
        password (str): This is password of the user.
        first_name (str): This is the first name of the user.
        last_name (str): And this is thelast name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
