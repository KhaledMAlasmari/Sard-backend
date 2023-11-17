from flask import Flask, g
from flask_expects_json import expects_json
from utils.schema.story_schema import generate_story_schema

app = Flask(__name__)


@app.route("/generate_story", methods=["POST"])
@expects_json(generate_story_schema)
def generate_story():
    print(g.data)
    return "", 200


@app.route("/health")
def hello():
    return "", 201
