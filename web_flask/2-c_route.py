""" Flask model for route"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Hello Route"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """HBNB Route"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def cee(text):
    """C Route"""
    return "C" + text.replace('_', ' ')
 
if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5000
    )