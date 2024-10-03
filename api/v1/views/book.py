#!/usr/bin/python3
""" Module for book view """
from api.v1.views import app_views
from flask import jsonify, abort, request, make_response
from models import storage
from models.book import Book
from models.user import User
from werkzeug.utils import secure_filename
import os


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app_views.route('/books', methods=['GET'], strict_slashes=False)
def get_Allbooks():
    """ Returns all books """
    
    books = [book.to_dict() for book in storage.all(Book).values()]
    
    return jsonify(books)


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
    """ Deletes a book along with its image file """
    
    book = storage.get(Book, book_id)
    if not book:
        abort(404)

    # Delete the associated image file
    if book.image:
        image_path = os.path.join('web_dynamic/static/uploads/images/', book.image)
        if os.path.exists(image_path):
            os.remove(image_path)

    storage.delete(book)
    storage.save()
    
    return make_response(jsonify({}), 200)


@app_views.route('users/<user_id>/books', methods=['POST'], strict_slashes=False)
def post_book(user_id):
    user = storage.get(User, user_id)
    if not user:
        abort(404)

    book_json = request.form.to_dict()

    if not book_json:
        abort(400, 'Not a valid form submission')
    
    # Handle file upload
    if 'image' in request.files:
        file = request.files['image']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            
            # Create the directory if it doesn't exist
            upload_folder = 'web_dynamic/static/uploads/images/'
            os.makedirs(upload_folder, exist_ok=True)
            
            file.save(os.path.join(upload_folder, filename))
            book_json['image'] = filename
        else:
            abort(400, 'Invalid file type')

    book_json['user_id'] = user_id
    book_json['status'] = "Available"
    book = Book(**book_json)
    book.save()

    return make_response(jsonify(book.to_dict()), 201)


@app_views.route('/books/<book_id>', methods=['PUT'], strict_slashes=False)
def put_book(book_id):
    """ Updates a book """
    
    book = storage.get(Book, book_id)
    if not book:
        abort(404)
        
    book_json = request.form.to_dict()

    if not book_json:
        abort(400, 'Not a valid form submission')

    # Handle image upload
    if 'image' in request.files:
        file = request.files['image']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            
            # Create the directory if it doesn't exist
            upload_folder = 'web_dynamic/static/uploads/images/'
            os.makedirs(upload_folder, exist_ok=True)
            
            file.save(os.path.join(upload_folder, filename))
            book_json['image'] = filename
        else:
            abort(400, 'Invalid file type')

    for key, value in book_json.items():
        if key not in ['id', 'user_id', 'created_at', 'updated_at']:
            setattr(book, key, value)
            
    book.save()
    
    return make_response(jsonify(book.to_dict()), 200)