#!/usr/bin/python3
""" Module for user view """
from api.v1.views import app_views
from flask import jsonify, abort, request, make_response
from models import storage
from models.user import User


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """ Returns all users """
    
    users = storage.all(User).values()
    users = [user.to_dict() for user in users]
    
    return jsonify(users)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """ Returns a user """
    
    user = storage.get(User, user_id)
    if not user:
        abort(404)
        
    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """ Deletes a user """
    
    user = storage.get(User, user_id)
    if not user:
        abort(404)
        
    storage.delete(user)
    storage.save()
    
    return make_response(jsonify({}), 200)


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def post_user():
    """ Creates a user """
    
    user_json = request.get_json()
    
    if not user_json:
        abort(400, 'Not a JSON')
    if 'email' not in user_json:
        abort(400, 'Missing email')
    if 'password' not in user_json:
        abort(400, 'Missing password')
    if 'first_name' not in user_json:
        abort(400, 'Missing first_name')
    if 'last_name' not in user_json:
        abort(400, 'Missing last_name')
    if 'user_name' not in user_json:
        abort(400, 'Missing username')
    if 'location' not in user_json:
        abort(400, 'Missing location')
        
    user = User(**user_json)
    user.save()
    
    return make_response(jsonify(user.to_dict()), 201)


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def put_user(user_id):
    """ Updates a user """
    
    user_json = request.get_json()
    
    if not user_json:
        abort(400, 'Not a JSON')
        
    user = storage.get(User, user_id)
    if not user:
        abort(404)
        
    for key, value in user_json.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(user, key, value)
            
    user.save()
    
    return make_response(jsonify(user.to_dict()), 200)


# authentification
@app_views.route('/login', methods=['POST'], strict_slashes=False)
def login():
    """ Login """
    
    data = request.get_json()
    username = data.get('user_name')
    password = data.get('password')
    
    if not username or not password:
        abort(400, description='Bad Request: Missing username or password')
    
    users = storage.all(User).values()
    for user in users:
        if user.user_name == username and user.password == password:
            response = make_response(jsonify(user.to_dict()), 200)
            
            return response
    
    abort(401, description='Unauthorized: Incorrect username or password')