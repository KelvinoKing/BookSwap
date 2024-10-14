#!/usr/bin/python3
""" Flask app """
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """ Return a simple string """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='localhost', port=5000)
