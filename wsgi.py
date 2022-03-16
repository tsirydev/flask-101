# wsgi.py
# pylint: disable=missing-docstring

from flask import jsonify
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/v1/products')
def products():
    return jsonify({
        1:{"id": 1, "name": "Skello"},
        2:{"id": 2, "name": "Socialive.tv"}
    })
