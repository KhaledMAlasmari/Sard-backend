from flask import Flask, g,Response
import base64
from flask_socketio import SocketIO, send, emit, join_room, leave_room
from flask_expects_json import expects_json
from services.story_generator import generate_story
from services.translation import translate_complete
from services.audio_genrator import text_to_audio_openai
from utils.schema.story_schema import generate_story_schema
from models.genres import Genres
from models.authors import Authors
import jsonschema
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*", max_http_buffer_size=300e8)

@socketio.on("generate_story")
def handle_generate_story(data):
    # validation, if valid it does not return anything otherwise it raises an exception which is caught by the error handler
    #print(data)
    jsonschema.validate(data, generate_story_schema)
    generated_story = generate_story(data)
    emit("generated_story", {"story": generated_story})


@socketio.on("translate_chapter")
def translate_chapter(data):
    chapter_id = data.get('chapterId')
    text = data.get('text')
    if not text or chapter_id is None:
        emit("error", {"message": "Missing text or chapterId"})
        return

    try:
        arabic_translation = translate_complete(text)
        print(arabic_translation)
        emit("translatred_story", {"chapterId": chapter_id, "translatedText": arabic_translation})
    except Exception as e:
        emit("error", {"message": str(e)})
        print(f"Error translating chapter {chapter_id}: {str(e)}")
        
@socketio.on('text_to_audio')
def gen_audio(text):
    base64_audio = text_to_audio_openai(text)
    emit("audio_story", {"audio": base64_audio})


@app.route("/genres", methods=["GET", "OPTIONS"])
def get_genres():
    return {"genres": Genres.get_all_genres()}, 200


@app.route("/authors", methods=["GET"])
def get_authors():
    return {"authors": Authors.get_all_authors()}, 200


@socketio.on_error_default  # handles all namespaces without an explicit error handler
def default_error_handler(e):
    error_message = str(e)  # Convert the exception to a string
    print("An error occurred:", error_message)
    emit("error", {"error": error_message})


# health check endpoint
@app.route("/health")
def hello():
    return "", 201


if __name__ == "__main__":
    socketio.run(app, debug=True)
