#!/usr/bin/python3
"""This is the Book class"""
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Text, ForeignKey
from sqlalchemy.orm import relationship


class Book(BaseModel, Base):
    """This is the Book class"""
    
    __tablename__ = 'books'
    title = Column(String(128), nullable=False)
    author = Column(String(128), nullable=False)
    synopsis = Column(String(128), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    genre = Column(String(128), nullable=False)
    status = Column(String(128), nullable=False)
    image = Column(String(128), nullable=False)
    user = relationship('User', back_populates='books')
