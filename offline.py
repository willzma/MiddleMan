from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import subprocess as sp
import sys, errno
import os

#ffmpegCmd =["ffmpeg", "-i", "-", "test%0d.bmp"]
#ffmpeg = sp.Popen(ffmpegCmd, stdin=sp.PIPE)
#ffmpegCmd =['ffmpeg', '-i', '-', '-pix_fmt', 'bgr24', '-f', 'image2pipe', '-']
#ffmpeg = sp.Popen(ffmpegCmd, stdin=sp.PIPE)

with open("/Users/ChaityaShah/Downloads/test.h264", 'rb') as f:
    byte_s = f.read(55376)
    #ffmpeg.stdin.write(byte_s)
    try:
        sys.stdout.buffer.write(byte_s)
    except IOError:
        print("err")

    with open("/Users/ChaityaShah/Downloads/test1.h264", 'ab') as f1:
            #f1.write(byte_s)
            print(len(byte_s))
    while len(byte_s) != 0:
        byte_s = f.read(100000000)
        #ffmpeg.stdin.write(byte_s)
        try:
            sys.stdout.buffer.write(byte_s)
        except IOError:
            print("err")
        with open("/Users/ChaityaShah/Downloads/test1.h264", 'ab') as f1:
            #f1.write(byte_s)
            print(len(byte_s))
    print("done")