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
    return """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If
 you entered the URL manually please check your spelling and try again.</p>
"""


@app.route('/c/<text>')
def C(text):
    """C is fun"""
    return f"C {text.replace('_', ' ')}"


@app.route('/python', defaults={'text': "is cool"})
@app.route('/python/<text>')
def python(text):
    """Python is cool"""
    return f"Python {text.replace('_', ' ')}"


def convert_or_404(value, type):
    """Convert a value to the given type, or raise a 404 error"""
    try:
        return type(value)
    except ValueError:
        abort(404)


@app.route('/number/<n>')
def number(n):
    """print number"""
    value = convert_or_404(n, int)
    return f"{value} is a number"


if __name__ == "__main__":
    # python -m api.v1.app
    app.run(host="0.0.0.0", port=5000)
