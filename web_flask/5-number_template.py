#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Hello Flask! """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """ HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ Print C<text> """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """ Print python texts, default ('is cool'). """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:num>', strict_slashes=False)
def number(num):
    """ It's a number! """
    if type(num) == int:
        return ("{} is a number".format(num))


@app.route('/number_template/<int:num>', strict_slashes=False)
def display_html(num):
    """ Display a HTML page. """
    if type(num) == int:
        return render_template('5-number.html', n=num)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
