#!/usr/bin/python3
""" flask module """
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """ list all states"""
    not_found = False
    if id is not None:
        states = storage.all(State, id)
        id_ava = True

        if len(states) == 0:
            not_found = True
    else:
        states = storage.all(State)
        id_ava = False

    return render_template('9-states.html', states=states,
                           id_ava=id_ava, not_found=not_found)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
