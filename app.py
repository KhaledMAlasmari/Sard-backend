from flask import Flask, g
from flask_socketio import SocketIO, send, emit,join_room, leave_room
from flask_expects_json import expects_json
from utils.schema.story_schema import generate_story_schema
from models.genres import Genres
from models.authors import Authors

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return "SocketIO Story Generator"

@socketio.on('generate_story')
# @expects_json(generate_story_schema)
def handle_generate_story(data):
    room = data['room']
    story = "my story!"
    emit("story",story, to=room)

@socketio.on('connect')
def test_connect(auth):
    emit('my response', {'data': 'Connected'})

@app.route("/genres", methods=["GET"])
def get_genres():
    return {"genres": Genres.get_all_genres()}, 200


@app.route("/authors", methods=["GET"])
def get_authors():
    return {"authors": Authors.get_all_authors()}, 200


@app.route("/health")
def hello():
    return "", 201

if __name__ == '__main__':
    socketio.run(app, debug=True)
