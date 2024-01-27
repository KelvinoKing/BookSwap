#!/usr/bin/python3
"""This is the Book class"""
from models.base_model import BaseModel
from models.user import User


class Book(BaseModel):
    """This is the Book class"""
    title = ""
    author = ""
    synopsis = ""
    owner_id = ""
    borrower_id = ""
    status = ""
    image = ""