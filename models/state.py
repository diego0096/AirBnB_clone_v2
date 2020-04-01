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
        obj = models.storage.all()
        for cls_name_id, cls_instance in obj.items():
            cls_name = cls_name_id.split(".")[0]
            if cls_name == "City":
                if cls_instance.state_id == self.id:
                    cities_instances.append(cls_instance)
        return cities_instances
