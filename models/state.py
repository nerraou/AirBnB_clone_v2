#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base, orm
from models.city import City
from sqlalchemy import Column, String


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = orm.relationship(
        'City',
        cascade='all, delete, delete-orphan',
        backref='state'
    )

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """
            returns the list of City instances
            with state_id equals to the current State.id
            """
            from models import storage
            cities_list = []
            cities_objs = storage.all(City)

            for city in cities_objs.values():
                if city.id == self.id:
                    cities_list.append(city)

            return cities_list
