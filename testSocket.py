import socketio

sio = socketio.Client()

@sio.event
def connect():
    print("Connected to server")

@sio.event
def disconnect():
    print("Disconnected from server")

@sio.event
def generated_story(data):
    print("Received generated story:", data)
    sio.disconnect()


@sio.event
def error(data):
    print("Received an error:", data)
    sio.disconnect()

if __name__ == "__main__":
    server_url = "ws://127.0.0.1:5000"
    sio.connect(server_url)
    
    message_to_send = {"guy": "khaled"}
    sio.emit("generate_story", message_to_send)
    
    sio.wait()
