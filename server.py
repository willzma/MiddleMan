from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('data')
def test_message(message):
    f = open("/Users/ChaityaShah/Downloads/test.h264", 'ab')
    #emit('my response', {'data': 'got it!'})
    print(len(message))
    f.write(message);

if __name__ == '__main__':
    socketio.run(app, port=8080)
