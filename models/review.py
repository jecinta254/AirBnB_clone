#!/usr/bin/python3
"""Definition of the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This class defines the class

    Attributes:
        place_id (str): This is the Place id.
        user_id (str): This is the User id.
        text (str): This is a text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
