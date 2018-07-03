import os
import cv2
import subprocess as sp
import sys, errno
from queue import Queue, Empty
from threading  import Thread
import numpy as np
import time

try:
    serverCmd =['python3', 'server.py']
    server = sp.Popen(serverCmd, stdout=sp.PIPE)
    ffmpegCmd = ['ffmpeg', '-i', '-', '-f', 'rawvideo', '-vcodec', 'bmp', '-vf', 'fps=10', '-']
    ffmpeg = sp.Popen(ffmpegCmd, stdin = server.stdout, stdout = sp.PIPE)

    while True:
        '''
        arr = []
        if initial:
            test = ffmpeg.stdout.read(1)
            while test[0] == 0:
                print("0")
                test = ffmpeg.stdout.read(1)
            arr.append(test)
            initial = False
        fileSizeBytes = ffmpeg.stdout.read(3)
        arr.append(list(fileSizeBytes))
        '''
        #fileSizeBytes = bytearray(arr)
        fileSizeBytes = ffmpeg.stdout.read(6)
        #print(len(fileSizeBytes))
        #fileSizeBytes = fileSizeBytes + ffmpeg.stdout.read(4)
        fileSize = 0
        #print(len(fileSizeBytes))
        #print(len(bytearray([fileSizeBytes[2]])))
        if len(fileSizeBytes) != 0:
            for i in range(4):
                fileSize += bytearray([fileSizeBytes[i+2]])[0] * 256 ** i
            if fileSize != 0:
                bmpData = fileSizeBytes + ffmpeg.stdout.read(fileSize - 6)
                image = cv2.imdecode(np.fromstring(bmpData, dtype = np.uint8), 1)
                cv2.imshow("im",image) 
                cv2.waitKey(2)
                if image is None:
                    print("meem")
                else:
                    print("the past tense of yeet is yote")
        else:
            print('rip')

except KeyboardInterrupt:
    try:
        server.terminate()
        ffmpeg.terminate()
    except OSError:
        pass