#!/usr/bin/python3
""" Flask app """
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Example data for books and users
books = [
    {'id': 1, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'owner': 'Alice', 'genre': 'Fiction', 'synopsis': 'A story about...'},
    {'id': 2, 'title': '1984', 'author': 'George Orwell', 'owner': 'Bob', 'genre': 'Dystopian', 'synopsis': 'A totalitarian regime...'}
]

user_books = [
    {'id': 1, 'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger'},
    {'id': 2, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'}
]

user = {'username': 'Alice'}

# Example chat data
chats = [
    {'sender': 'Bob', 'last_message': 'Can I borrow The Great Gatsby?', 'read': False},
    {'sender': 'Charlie', 'last_message': 'Do you have any other books?', 'read': True},
    {'sender': 'Bob', 'last_message': 'Thanks for the book!', 'read': True}
]

# Other users (simulated)
other_users = [
    {'username': 'Bob'},
    {'username': 'Charlie'},
    {'username': 'David'}
]


@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/books')
def books_page():
    return render_template('books.html', books=books)

@app.route('/profile')
def profile():
    return render_template('profile.html', user=user, user_books=user_books, other_users=other_users)


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        # Get form data and create a new book entry
        new_id = len(user_books) + 1
        new_book = {
            'id': new_id,
            'title': request.form['title'],
            'author': request.form['author']
        }
        user_books.append(new_book)
        return redirect(url_for('profile'))

    return render_template('add_book.html')

@app.route('/update_book/<int:book_id>', methods=['GET', 'POST'])
def update_book(book_id):
    # Find the book to update
    book = next((book for book in user_books if book['id'] == book_id), None)
    if request.method == 'POST':
        # Update book details
        if book:
            book['title'] = request.form['title']
            book['author'] = request.form['author']
        return redirect(url_for('profile'))

    return render_template('update_book.html', book=book)

@app.route('/delete_book/<int:book_id>')
def delete_book(book_id):
    # Remove the book from user's collection
    global user_books
    user_books = [book for book in user_books if book['id'] != book_id]
    return redirect(url_for('profile'))

if __name__ == '__main__':
    app.run(debug=True)
