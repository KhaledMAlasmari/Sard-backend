# save this as app.py
from flask import Flask, request, jsonify, Response

from ai.image_to_text import ImageToText

app = Flask(__name__)

@app.route('/generate_story', methods=['POST'])
def generate_story():
    pass


@app.route("/health")
def hello():
    return "", 201
