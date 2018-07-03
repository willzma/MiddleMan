from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import subprocess as sp
import sys, errno
import os

app = Flask(__name__)
socketio = SocketIO(app)

#ffmpeg -i - -f rawvideo "test%0d.bmp"

#ffmpeg -i "test.h264" "test%0d.bmp"
ffmpegCmd =["ffmpeg", "-i", "-", "test%0d.bmp"]
ffmpeg = sp.Popen(ffmpegCmd, stdin=sp.PIPE)
@socketio.on('data')
def test_message(message):
    print("meme")
    with open("/Users/ChaityaShah/Downloads/test.h264", 'ab') as f:
        if message != None:
            print(len(message))
            f.write(message)
            #os.write(1, message)
            
            try:
                #print('doesn"t work')
                ffmpeg.stdin.write(message)
                #ffmpeg.communicate()
            except IOError as e:
                if e.errno == errno.EPIPE:
                    print("err")
            

@socketio.on('terminate')
def suicide(message_count):
    print(message_count)


if __name__ == '__main__':
    print("Running")
    socketio.run(app, port=8080)
