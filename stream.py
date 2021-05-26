import cv2
import argparse
import socketio
import numpy as np
import base64

sio = socketio.Client()

# from socket_modules import sio, streaming

parser = argparse.ArgumentParser(description="Please enter your argument.")
parser.add_argument('--movie', required=False,
                    help='Please enter an video folder to import.')

args = parser.parse_args()

VIDEO_PATH = args.movie


class stream:
    def __init__(self):
        sio.connect('http://127.0.0.1:5000')
        self.run()

    def run(self):
        print(" Run !! ")
        # sio.connect()

        if VIDEO_PATH != None:
            cap = cv2.VideoCapture(VIDEO_PATH)
        else:
            cap = cv2.VideoCapture(0)

        while cap.isOpened():
            run, frame = cap.read()
            if not run:
                print(" Not Found Frame - Process Exit ")
                break

            img = cv2.cvtColor(frame, cv2.IMREAD_COLOR)
            sio.emit('streaming', {'img': str(img)})
            # sio.emit('streaming', "streaming-test")

            cv2.imshow('video', frame)
            k = cv2.waitKey(30)
            if k == 27:
                sio.disconnect()
                cv2.destoryAllWindows()

        cap.release()
        k = cv2.waitKey(30)
        if k == 27:
            sio.disconnect()
            cv2.destoryAllWindows()


@sio.event
def connect():
    print('connection established')


@sio.event
def disconnect():
    print('disconnected from server')


@sio.on('received')
def messageReceived(callback, methods=['GET', 'POST']):
    print('message was received!!!'+callback)


if __name__ == '__main__':
    stream()
