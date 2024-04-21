#!/usr/bin/python3
""" Flask web application"""

from models import storage
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def states():
    """
    all state data
    """

    states = storage.all("State")
    return render_template("8-cities_by_states.html",
                           states=states)


@app.teardown_appcontext
def terminate(exc):
    """
    Close session
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
