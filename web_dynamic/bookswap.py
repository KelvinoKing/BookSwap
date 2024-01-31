#!/usr/bin/python3
""" Flask app """
from flask import Flask, render_template, request
from models import storage
from models.book import Book
from models.user import User
import uuid
app = Flask(__name__)


@app.teardown_appcontext
def close_db(self):
    """ Close session """
    storage.close()
    
@app.route('/books', strict_slashes=False)
def books():
    """ BookSwap is live """
    
    books = storage.get_session().query(Book, User.user_name, User.location).join(
        User, 
        Book.user_id == User.id).all()
    
    cache_id = str(uuid.uuid4())
    
    return render_template('book.html',
                           books=books,
                           cache_id=cache_id)
    

@app.route('/home', strict_slashes=False)
def home():
    """ Home page """
    
    cache_id = str(uuid.uuid4())
    return render_template('index.html',
                           cache_id=cache_id)


@app.route('/about', strict_slashes=False)
def about():
    """ About page """
    
    cache_id = str(uuid.uuid4())
    return render_template('about.html',
                           cache_id=cache_id)
    
    
@app.route('/login', strict_slashes=False)
def login():
    """ Login page """
    
    cache_id = str(uuid.uuid4())
    return render_template('login.html',
                           cache_id=cache_id)
    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)