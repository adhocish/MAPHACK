from app import app
from flask import jsonify, request

@app.route("/")
def maphack():
    return "black sheep wall"