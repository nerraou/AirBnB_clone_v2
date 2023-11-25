#!/usr/bin/python3
"""
ARBNB CLONE
"""


from flask import Flask, abort, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_world():
    """hello hbnh"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """HBNB"""
    return "HBNB"


@app.errorhandler(404)
def not_found(error):
    """ json 404 page """
    return render_template("404.html")


@app.route('/c/<text>')
def C(text):
    """C is fun"""
    return f"C {text.replace('_', ' ')}"


@app.route('/python', defaults={'text': "is cool"})
@app.route('/python/<text>')
def python(text):
    """Python is cool"""
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>')
def number(n):
    """print number"""
    return f"{n} is a number"


if __name__ == "__main__":
    # python -m api.v1.app
    app.run(host="0.0.0.0", port=5000)
