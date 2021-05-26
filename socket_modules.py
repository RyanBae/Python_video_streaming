import socketio

sio = socketio.Client()


@sio.event
def connect():
    print('connection established')


@sio.event
def streaming(data):
    print('message received with ', data)
    sio.emit('streaming', {'response': 'my response'})


@sio.event
def disconnect():
    print('disconnected from server')


sio.connect('http://127.0.0.1:5000')
sio.wait()
