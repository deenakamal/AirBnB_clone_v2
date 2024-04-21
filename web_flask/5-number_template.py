#!/usr/bin/python3
"""
Flask web application
"""
from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """a function thay displays Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """a function that displays HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """with variable"""

    return f"C {escape(text.replace('_', ' '))}"


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """with varible"""

    return f"Python {escape(text.replace('_', ' '))}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n=None):
    """if n is integer display it"""
    return f"{n} is a number"

@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n=None):
    """html page if n is integer"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
