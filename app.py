from flask import Flask, g
from flask_socketio import SocketIO, send, emit, join_room, leave_room
from flask_expects_json import expects_json
from services.story_generator import generate_story
from utils.schema.story_schema import generate_story_schema
from models.genres import Genres
from models.authors import Authors
import jsonschema
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on("generate_story")
def handle_generate_story(data):
    # validation, if valid it does not return anything otherwise it raises an exception which is caught by the error handler
    #print(data)
    jsonschema.validate(data, generate_story_schema)
    generated_story = generate_story(data)
    emit("generated_story", {"story": generated_story})

@app.route("/genres", methods=["GET", "OPTIONS"])
def get_genres():
    return {"genres": Genres.get_all_genres()}, 200


@app.route("/authors", methods=["GET"])
def get_authors():
    return {"authors": Authors.get_all_authors()}, 200


@socketio.on_error_default  # handles all namespaces without an explicit error handler
def default_error_handler(e):
    print("An error occurred:", e)
    emit("error", {"error": e})


# health check endpoint
@app.route("/health")
def hello():
    return "", 201


if __name__ == "__main__":
    socketio.run(app, debug=True)
