from openai import OpenAI
import base64
from io import BytesIO
import os
from flask_socketio import emit

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def text_to_audio_openai(text):
    emit('progress', {'progress': 10})

    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
    )
    emit('progress', {'progress': 50})

    # If the response directly allows access to audio bytes, use it as is
    if hasattr(response, 'content'):
        audio_bytes = response.content  # This property needs to be confirmed with OpenAI documentation
    else:
        # Convert response to binary and handle as a BytesIO object
        audio_data = BytesIO()
        response.stream_to_file(audio_data)
        audio_data.seek(0)
        audio_bytes = audio_data.read()
            
    emit('progress', {'progress': 100})

    base64_audio = base64.b64encode(audio_bytes).decode('utf-8')
    return base64_audio