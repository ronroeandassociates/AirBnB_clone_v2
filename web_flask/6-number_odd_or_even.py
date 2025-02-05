#!/usr/bin/python3
"""FLASK"""
from flask import Flask
from flask.templating import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_only():
    """HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """c_route"""
    return f'C {text.replace("_", " ")}'


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is cool"):
    """python_route"""
    return f'Python {text.replace("_", " ")}'


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    if isinstance(n, int):
        return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """number_template"""
    if isinstance(n, int):
        return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    oe = "even" if n % 2 == 0 else "odd"
    return render_template("6-number_odd_or_even.html", n=n, oe=oe)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
