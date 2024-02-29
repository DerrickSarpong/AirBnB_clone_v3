#!/usr/bin/python3
"""
Defines a Flask web api for AirBNB clone
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_app_context(exc):
    storage.close()


@app.get("/states_list", strict_slashes=False)
def get_states_list():
    """Displays all states in an html page"""
    states = storage.all(State)
    states = sorted(states.values(), key=lambda val: val.name)
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
