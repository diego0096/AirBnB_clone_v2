#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
import os
import models


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """

    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if os.getenv("HBNB_TYPE_STORAGE") == 'db':
        cities = relationship("City", passive_deletes=True, backref="state")

    @property
    def cities(self):
        """ Return cities instances """
        cities_instances = []
        for city in models.storage.all(City).values():
            if self.id == city.state_id:
                cities_instances.append(city)
        return cities_instances
