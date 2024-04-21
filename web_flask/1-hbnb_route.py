#!/usr/bin/python3
"""
Flask web application.
"""""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """a function that diplays Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ a function that displays HBNB"""
    return "HBNB"


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
