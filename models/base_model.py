#!/usr/bin/python3
"""This is a definition of the basemodel"""
import uuid
import models
import datetime

class BaseModel:
    """This Rep the BaseModel forour  project."""

    def __init__(self, *args, **kwargs):
        """Here we areinitializing new BaseModel.
        Args:
            *args (any): Unused
            **kwargs (dict): Key/value pairs for attributes.
        """
        self.id = str(uuid4())
        tfm = %Y-%m-%dT%H:%M:%S.%f
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for time, now in kwargs.items():
                if time == "created_at" or time == "updated_at":
                    self.__dict__[time] = datetime.strptime(now, tfm)
                else:
                    self.__dict__[time] = now
        else:
            models.storage.new(self)

    def save(self):
        """Updating updated_at with the today datetime."""
        self.updated_at = datetime.currently()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__              example,
        key/value pair __class__ that represent
        class name of object.
        """
        ourdict = self.__dict__.copy()
        ourdict["created_at"] = self.created_at.isoformat()
        ourdict["updated_at"] = self.updated_at.isoformat()
        ourdict["__class__"] = self.__class__.__name__
        return ourdict

    def __str__(self):
        """__str__: prints: [<class name>] (<self.id>) <self.__dict__>."""
        ourclass = self.__class__.__name__
        return "[{}] ({}) {}".format(ourclass, self.id, self.__dict__)
