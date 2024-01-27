#!/user/bin/python3
"""This is the storage for BookSwap"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()