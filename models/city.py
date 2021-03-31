#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import os


class City(BaseModel):
    """ The city class, contains state ID and name """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "cities"
        state_id = Column(String(128), nullable=False)
        name = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", backref="cities,
                              cascade="all, delete-orphan")
    else:
        name = ""
        state_id = ""
