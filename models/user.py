#!/usr/bin/python3
"""This is the User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """This is the User class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    location = ""
    user_name= ""