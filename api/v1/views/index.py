#!/usr/bin/python3
""" Module for index view """
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.user import User
from models.book import Book


@app_views.route('/status', strict_slashes=False)
def status():
    """ Returns status """
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def stats():
    """ Returns stats """
    
    classes = [User, Book]
    names = ["users", "books"]
    
    num_objects = {}
    for i in range(len(classes)):
        num_objects[names[i]] = storage.count(classes[i])
        
    return jsonify(num_objects)
   