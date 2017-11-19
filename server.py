from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('data')
def test_message(message):
    #f = open("/Users/ChaityaShah/Downloads/test.h264", 'ab')
    print(len(message))
    #f.write(message)

@socketio.on('terminate')
def suicide(message_count):
    print(message_count)


if __name__ == '__main__':
    socketio.run(app, port=8080)
