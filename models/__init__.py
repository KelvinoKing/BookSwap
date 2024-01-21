#!/usr/bin/python3
"""uses file storage to manage data for my BookSwap project"""
from models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()