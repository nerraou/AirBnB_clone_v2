#!/usr/bin/python3
"""
ARBNB CLONE
"""


from flask import Flask, jsonify, make_response

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
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    # python -m api.v1.app
    app.run(host="0.0.0.0", port=5000)
