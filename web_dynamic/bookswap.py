#!/usr/bin/python3
""" Flask app """
from flask import Flask, render_template, request, session, abort, redirect, url_for, flash
from models import storage
from models.book import Book
from models.user import User
import uuid
from flask_cors import CORS
from flask_login import LoginManager
from flask_login import login_user, login_required, current_user, logout_user


app = Flask(__name__)
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)
CORS(app, origins=['http://127.0.0.1:5001'], supports_credentials=True)
app.secret_key = 'Kelvino2001@king'


@login_manager.user_loader
def load_user(user_id):
    """ Load user """
    return storage.get(User, user_id)


@app.teardown_appcontext
def close_db(self):
    """ Close session """
    storage.close()
    

@app.route('/home', strict_slashes=False)
def home():
    """ Home page """
    
    cache_id = str(uuid.uuid4())
    return render_template('index.html',
                           cache_id=cache_id)
    
    
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


@app.route('/about', strict_slashes=False)
def about():
    """ About page """
    
    cache_id = str(uuid.uuid4())
    return render_template('about.html',
                           cache_id=cache_id)
    
    
@app.route('/dashboard', strict_slashes=False)
@login_required
def dashboard():
    """ Dashboard route """
        
    user = storage.get(User, current_user.id)
    if not user:
        abort(401)
        
    user = user.to_dict()
    books = storage.get_session().query(Book).filter(
        Book.user_id == session['user_id']).all()
    
        
    cached_id = str(uuid.uuid4())
    # Render the dashboard template with user data
    return render_template('dashboard.html',
                           user=user,
                            books=books,
                           cache_id=cached_id)
    

# authentification
@app.route('/login', strict_slashes=False)
def login():
    """ Login """
    
    cached_id = str(uuid.uuid4())
    return render_template('login.html',
                           cache_id=cached_id)


@app.route('/signup', methods=['POST'], strict_slashes=False)
def signup():
    """ Signup """
    
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
        
    user = storage.get_session().query(User).filter_by(email=user_json['email']).first()
    if user:
        flash('Email address already exists')
        return redirect(url_for('login'))
            
    user = User(**user_json)
    user.save()
    
    flash('Sign up successful. Now you can proceed to sign in')
    return redirect(url_for('login'))


@app.route('/signin', methods=['POST'], strict_slashes=False)
def signin():
    """Signin"""
    
    data = request.get_json()
    username = data.get('user_name')
    password = data.get('password')
    
    if not username or not password:
        flash('Missing username or password')
        abort(400, description='Bad Request: Missing username or password')
        
    users = storage.all(User).values()
    for user in users:
        if user.user_name == username and user.password == password:
            login_user(user, remember=True)
            session['user_id'] = user.id
        
    flash("Incorect logins. Try again.")
    return redirect(url_for('login'))
    

@app.route('/logout', strict_slashes=False)
@login_required
def logout():
    """ Logout """
    
    user = storage.get(User, current_user.id)
    if not user:
        abort(401)
    
    logout_user()
    return redirect(url_for('books'))
    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)