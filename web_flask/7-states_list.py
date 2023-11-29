#!/usr/bin/python3
"""
ARBNB CLONE
"""


from flask import Flask, render_template
from models import storage
from models.state import State

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


@app.route('/number_template/<int:n>')
def number_template(n):
    """print number"""
    return render_template("5-number.html", number=n)


@app.route('/number_odd_or_even/<int:n>')
def number_template_oddity(n):
    """print number oddity"""
    odd = "odd"
    if n % 2 == 0:
        odd = "even"
    return render_template("6-number_odd_or_even.html", number=n, oddity=odd)


@app.route("/states_list")
def states_list():
    """list all states"""
    states = storage.all(State)

    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """close sessions"""
    storage.close()


if __name__ == "__main__":
    # python -m api.v1.app
    app.run(host="0.0.0.0", port=5000)
