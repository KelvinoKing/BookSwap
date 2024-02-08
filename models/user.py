#!/usr/bin/python3
"""This is the User class"""
from models.base_model import BaseModel, Base
from models.book import Book
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from flask_login import UserMixin


class User(UserMixin, BaseModel, Base):
    """This is the User class"""
    
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    location = Column(String(128), nullable=False)
    user_name= Column(String(128), nullable=False)
    books = relationship('Book',
                         back_populates='user',
                         cascade='all, delete, delete-orphan')
    
    chats = relationship('Chat', back_populates='user')