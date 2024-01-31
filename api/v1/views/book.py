#!/usr/bin/python3
""" Module for book view """
from api.v1.views import app_views
from flask import jsonify, abort, request, make_response
from models import storage
from models.book import Book
from models.user import User


@app_views.route('users/<user_id>/books', methods=['GET'], strict_slashes=False)
def get_books(user_id):
    """ Returns all books """
    
    user = storage.get(User, user_id)
    if not user:
        abort(404)
        
    books = [book.to_dict() for book in user.books]
    
    return jsonify(books)


@app_views.route('/books/<book_id>', methods=['GET'], strict_slashes=False)
def get_book(book_id):
    """ Returns a book """
    
    book = storage.get(Book, book_id)
    if not book:
        abort(404)
        
    return jsonify(book.to_dict())


@app_views.route('/books/<book_id>', methods=['DELETE'], strict_slashes=False)
def delete_book(book_id):
    """ Deletes a book """
    
    book = storage.get(Book, book_id)
    if not book:
        abort(404)
        
    storage.delete(book)
    storage.save()
    
    return make_response(jsonify({}), 200)


@app_views.route('users/<user_id>/books', methods=['POST'], strict_slashes=False)
def post_book(user_id):
    """ Creates a book """
    
    user = storage.get(User, user_id)
    if not user:
        abort(404)
        
    book_json = request.get_json()
    
    if not book_json:
        abort(400, 'Not a JSON')
    if 'title' not in book_json:
        abort(400, 'Missing title')
    if 'author' not in book_json:
        abort(400, 'Missing author')
    if 'synopsis' not in book_json:
        abort(400, 'Missing synopsis')
    if 'genre' not in book_json:
        abort(400, 'Missing genre')
    if 'status' not in book_json:
        abort(400, 'Missing status')
    if 'image' not in book_json:
        abort(400, 'Missing image')
        
    book_json['user_id'] = user_id
    book = Book(**book_json)
    book.save()
    
    return make_response(jsonify(book.to_dict()), 201)


@app_views.route('/books/<book_id>', methods=['PUT'], strict_slashes=False)
def put_book(book_id):
    """ Updates a book """
    
    book = storage.get(Book, book_id)
    if not book:
        abort(404)
        
    book_json = request.get_json()
    
    if not book_json:
        abort(400, 'Not a JSON')
        
    for key, value in book_json.items():
        if key not in ['id', 'user_id', 'created_at', 'updated_at']:
            setattr(book, key, value)
            
    book.save()
    
    return make_response(jsonify(book.to_dict()), 200)