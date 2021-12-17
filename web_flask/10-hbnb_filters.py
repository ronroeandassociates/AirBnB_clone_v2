#!/usr/bin/python3
'''Flask app for hbnb filters'''


from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb_filters')
def hbnbFilters():
    return render_template('10-hbnb_filters.html',
                           states=storage.all(State),
                           amenities=storage.all(Amenity))


@app.teardown_appcontext
def teardown(context):
    storage.close()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
