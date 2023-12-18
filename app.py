from flask import Flask, g
from flask_expects_json import expects_json
from utils.schema.story_schema import generate_story_schema
from models.genres import Genres
from models.authors import Authors

app = Flask(__name__)


@app.route("/generate_story", methods=["POST"])
@expects_json(generate_story_schema)
def generate_story():
    print(g.data)
    return "", 200


@app.route("/genres", methods=["GET"])
def get_genres():
    return Genres.get_all_genres(), 200


@app.route("/authors", methods=["GET"])
def get_authors():
    return Authors.get_all_authors(), 200


@app.route("/health")
def hello():
    return "", 201
