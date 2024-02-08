#!/usr/bin/python3
"""This is the Chat class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, Text


class Chat(BaseModel, Base):
    """This is the Chat class"""
    
    __tablename__ = 'chats'
    sender_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    receiver_id = Column(String(60), nullable=False)
    message = Column(Text, nullable=False)
    sender = Column(String(60), nullable=False)
    receiver = Column(String(60), nullable=False)
    user = relationship('User', back_populates='chats')