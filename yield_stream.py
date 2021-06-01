import cv2
import argparse
import socketio
import numpy as np
import base64

# https://medium.datadriveninvestor.com/video-streaming-using-flask-and-opencv-c464bf8473d6

sio = socketio.Client()

parser = argparse.ArgumentParser(description="Please enter your argument.")
parser.add_argument('--movie', required=False,
                    help='Please enter an video folder to import.')

args = parser.parse_args()

VIDEO_PATH = args.movie


class yield_stream:
    def __init__(self):
        con = sio.connect('http://127.0.0.1:5000')
        self.run()

    def run(self):
        print("Run !! ")

        if VIDEO_PATH != None:
            cap = cv2.VideoCapture(VIDEO_PATH)
        else:
            cap = cv2.VideoCapture(0)

        # g = []

        # while cap.isOpened():
        #     run, frame = cap.read()
        #     if not run:
        #         print(" Not Found Frame - Process Exit ")
        #         self.process_exit()
        #         break
        #     else:
        #         img = cv2.cvtColor(frame, cv2.IMREAD_COLOR)
        #         jpg_img = cv2.imencode('.jpg', img)
        #         b64_string = base64.b64encode(jpg_img[1]).decode('utf-8')
        #         g = self.gen(b64_string)
        #         print("=====================")
        #         print(type(g))
        #         # print(next(g))
        #         base_str = next(g)
        #         print(base_str)

        #         sio.emit('streaming', {'img': base_str})
        #         # yield str(b64_string)
        #         # print()
        #         # sio.emit()
        #         height, width, channel = img.shape
        #         im2 = cv2.resize(frame, dsize=(0, 0), fx=0.6, fy=0.6,
        #                          interpolation=cv2.INTER_AREA)
        #         im = cv2.imshow('video', im2)
        #         k = cv2.waitKey(30)
        #         if k == 27:
        #             self.process_exit()
        g = cap.read()
        # yield frame
        print('------!')
        print(g)
        # run, frame = next(g)
        # im = cv2.imshow('video', frame)
        # for i in len(g)
        # print(i)

        g2 = self.example_gen()
        print(type(g2))
        print(next(g2))
        print(next(g2))
        print(next(g2))
        print(next(g2))

        # cap.release()
        # k = cv2.waitKey(30)
        # if k == 27:
        # self.process_exit()

    def gen(self, base64):
        yield base64

    def example_gen(self):
        yield 1
        yield 2
        yield 3
        yield 4

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
    yield_stream()
