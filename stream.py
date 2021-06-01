import cv2
import argparse
import socketio
import numpy as np
import base64

sio = socketio.Client()

# from socket_modules import sio, streaming
# python3 stream.py --movie=./video/cat_video.mp4
# python3 stream.py

parser = argparse.ArgumentParser(description="Please enter your argument.")
parser.add_argument('--movie', required=False,
                    help='Please enter an video folder to import.')

args = parser.parse_args()

VIDEO_PATH = args.movie


class stream:
    def __init__(self):
        con = sio.connect('http://0.0.0.0:5000')
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
                self.process_exit()
                break

            img = cv2.cvtColor(frame, cv2.IMREAD_COLOR)
            jpg_img = cv2.imencode('.jpg', img)
            b64_string = base64.b64encode(jpg_img[1]).decode('utf-8')
            sio.emit('streaming', {'img': str(b64_string)})
            # sio.emit('streaming', "streaming-test")
            height, width, channel = img.shape
            im2 = cv2.resize(frame, dsize=(0, 0), fx=0.6, fy=0.6,
                             interpolation=cv2.INTER_AREA)
            im = cv2.imshow('video', im2)
            k = cv2.waitKey(30)
            if k == 27:
                self.process_exit()

        cap.release()
        k = cv2.waitKey(30)
        if k == 27:
            self.process_exit()

    def process_exit(self):
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
