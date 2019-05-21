from colorama import Fore, Style
from log import log

import eventlet
import socketio

tsj = 'text/javascript'

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/':
        {'content_type': 'text/html', 'filename': 'index.html'},
    '/socket.io':
        {'content_type': tsj, 'filename': 'public/js/socket.io.js'},
    '/client.js':
        {'content_type': tsj, 'filename': 'public/js/client.js'},
    '/scenes/login.js':
        {'content_type': tsj, 'filename': 'public/js/scenes/login.js'},
    '/scenes/game.js':
        {'content_type': tsj, 'filename': 'public/js/scenes/game.js'}
})


@sio.on('connect')
def connect(sid, env):
    log('server', 'Connected: ' + sid)


@sio.on('login')
def login(sid, login_info):
    log('server', f'Login: {Fore.GREEN}' + str(login_info)
        + f'{Style.RESET_ALL} (' + sid + ')')

    sio.emit(
        'login_success',
        {
            'user_info': {
                'username': login_info['username']
            }
        },
        room=sid)


@sio.on('disconnect')
def disconnect(sid):
    log('server', 'Disconnected: ' + sid)


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 3000)), app)
