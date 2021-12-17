#!/usr/bin/python3
"""FLASK"""
if __name__ == '__main__':
    from flask import Flask
    from flask import render_template

    app = Flask(__name__)
    app.url_map.strict_slashes = False

    @app.route('/')
    def hello_HBNB():
        """[This stes the route for hello_hbnb]
        """
        return "Hello HBNB!"

    @app.route('/hbnb')
    def HBNB():
        """[This route displays HBHB]
        """
        return "HBNB"

    @app.route('/c/<text>')
    def print_C(text):
        """[/c/<text> Displays C followed by the value of the text]
        """
        new_str = text.replace('_', ' ')
        return "C {}".format(new_str)

    @app.route('/python/', defaults={'text': 'is cool'})
    @app.route('/python/<text>')
    def print_python(text="is cool"):
        """[Prints python and gets rid of '_'
            if there are any]
        Args:
            text (str):Defaults to "is cool".
        """
        new_str = text.replace('_', ' ')
        return "Python {}".format(new_str)

    @app.route('/number/<int:n>')
    def display_n(n):
        """[display “n is a number” only if n is an integer]
        Args:
            n ([int]):
        """
        return "{} is a number".format(n)

    @app.route('/number_template/<int:n>')
    def number_template(n):
        """[This displays h1 tag]
        """
        return render_template('5-number.html', n=n)

    app.run(host='0.0.0.0', port='5000')
