#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime


class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """
        init base model
        get all values from kwargs
        """
        if len(kwargs) != 0:
            for key in kwargs:
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(kwargs[key]))
                else:
                    setattr(self, key, kwargs[key])
        else:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def update(self, **kwargs):
        "update with dict"
        for key in kwargs:
            if key == "__class__":
                continue
            if key == "created_at" or key == "updated_at":
                setattr(self, key, datetime.fromisoformat(kwargs[key]))
            else:
                setattr(self, key, kwargs[key])
