from log import log

import eventlet
import socketio

tsj = 'text/javascript'

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'},
    '/socket.io': {'content_type': tsj, 'filename': 'public/js/socket.io.js'},
    '/client.js': {'content_type': tsj, 'filename': 'public/js/client.js'},
})


@sio.on('connect')
def connect(sid, env):
    log('server', 'Connected: ' + sid)


@sio.on('disconnect')
def disconnect(sid):
    log('server', 'Disconnected: ' + sid)


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 3000)), app)
