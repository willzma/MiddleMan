from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import subprocess as sp
import sys, errno
import os


with open("/Users/ChaityaShah/Downloads/test.h264", 'rb') as f:
    byte_s = f.read(55376)
    try:
        sys.stdout.buffer.write(byte_s)
    except IOError:
        print("err")

    with open("/Users/ChaityaShah/Downloads/test1.h264", 'ab') as f1:
            print(len(byte_s))
    while len(byte_s) != 0:
        byte_s = f.read(100000000)
        try:
            sys.stdout.buffer.write(byte_s)
        except IOError:
            print("err")
        with open("/Users/ChaityaShah/Downloads/test1.h264", 'ab') as f1:
            print(len(byte_s))
    print("done")
