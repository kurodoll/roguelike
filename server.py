from colorama import Fore, Style
from log import log

from Game import Manager

import os
import eventlet
import socketio

game_manager = Manager.Manager()

tsj = 'text/javascript'
isp = 'image/png'

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
    '/scenes/gui.js':
        {'content_type': tsj, 'filename': 'public/js/scenes/gui.js'},
    '/scenes/game.js':
        {'content_type': tsj, 'filename': 'public/js/scenes/game.js'},
    '/graphics/tile/ground.png':
        {'content_type': isp, 'filename': 'public/graphics/tile/ground.png'}
})

sid_data = {}


@sio.on('connect')
def connect(sid, env):
    log('server', 'Connected: ' + sid)


@sio.on('login')
def login(sid, login_info):
    if sid not in sid_data:
        sid_data[sid] = {
            'login_info': login_info
        }
    else:
        sid_data[sid]['login_info'] = login_info

    log('server', f'Login: {Fore.GREEN}' + str(login_info)
        + f'{Style.RESET_ALL} (' + sid + ')')

    sio.emit(
        'login_success',
        {
            'username': login_info['username']
        },
        room=sid)

    on_level = game_manager.getPlayerLevel(login_info['username'])
    level = game_manager.getLevel(on_level)

    sio.emit('present_level', level, room=sid)


@sio.on('chat_msg')
def chat_msg(sid, msg):
    sender = sid_data[sid]['login_info']['username']

    log('chat', sender + f': {Fore.RED}' + msg + f'{Style.RESET_ALL}')

    sio.emit('chat_msg', {
        'from': sender,
        'msg': msg
    })


@sio.on('disconnect')
def disconnect(sid):
    log('server', 'Disconnected: ' + sid)


if __name__ == '__main__':
    port = 3000

    if os.environ['PORT']:
        port = os.environ['PORT']

    eventlet.wsgi.server(eventlet.listen(('', port)), app)
