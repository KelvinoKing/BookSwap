#!/usr/bin/python3
""" Module for chat view """
from api.v1.views import app_views
from flask import jsonify, abort, request, make_response, session
from models import storage
from models.chat import Chat
from models.user import User
from operator import itemgetter


@app_views.route('/chats', methods=['GET'], strict_slashes=False)
def get_chats():
    """ Returns all chats """
    chats = [chat.to_dict() for chat in storage.all(Chat).values()]
    
    # Sort chats based on the 'created_at' attribute
    sorted_chats = sorted(chats, key=itemgetter('created_at'))
    
    return jsonify(sorted_chats)


# @app_views.route('/users/<user_id>/chats', methods=['GET'], strict_slashes=False)
# def get_chats(user_id):
# """ Returns all chats """
#   user = storage.get(User, user_id)
#   if not user:
#        abort(404)
#    chats = [chat.to_dict() for chat in user.chats]
#    return jsonify(chats)

@app_views.route('/chats/<chat_id>', methods=['GET'], strict_slashes=False)
def get_chat(chat_id):
    """ Returns a chat """
    chat = storage.get(Chat, chat_id)
    if not chat:
        abort(404)
    return jsonify(chat.to_dict())


@app_views.route('/users/<user_id>/chats', methods=['POST'], strict_slashes=False)
def post_chat(user_id):
    """ Creates a chat """
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    chat_json = request.get_json()
    if not chat_json:
        abort(400, 'Not a JSON')
    if 'message' not in chat_json:
        abort(400, 'Missing message')
    if 'sender' not in chat_json:
        abort(400, 'Missing sender')
    if 'sender_id' not in chat_json:
        abort(400, 'Missing sender_id')
    if 'receiver' not in chat_json:
        abort(400, 'Missing receiver')
    if 'receiver_id' not in chat_json:
        abort(400, 'Missing receiver_id')
        
    chat = Chat(**chat_json)
    storage.new(chat)
    storage.save()
    return make_response(jsonify(chat.to_dict()), 201)