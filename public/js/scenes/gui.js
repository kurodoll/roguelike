class SceneGUI extends Phaser.Scene {
    constructor() {
        super({ key: 'gui' });

        this.valid_keys = [ 32 ];
        for (let i = 48; i <= 57; i++) {
            this.valid_keys.push(i);
        }
        for (let i = 65; i <= 90; i++) {
            this.valid_keys.push(i);
        }
    }

    create() {
        this.active_element = 'none';

        this.text_chat_input = this.add.text(
            $('canvas').width() - 400, $('canvas').height() - 20,
            '',
            { font: '8pt Verdana', fill: '#FFFFFF' })

        this.chat_msgs_history = [];
        this.text_chat_msgs = this.add.text(
            $('canvas').width() - 400, $('canvas').height() - 160,
            '',
            { font: '8pt Verdana', fill: '#FFFFFF' })

        this.input.keyboard.on('keydown', (key) => {
            if (this.active_element == 'none' && key.keyCode == 13) {
                this.active_element = 'chat'
            } else if (this.active_element == 'chat') {
                if (this.valid_keys.indexOf(key.keyCode) > -1) {
                    this.text_chat_input.text += key.key;
                } else if (key.keyCode == 13) {
                    socket.emit('chat_msg', this.text_chat_input.text);

                    this.text_chat_input.text = '';
                    this.active_element = 'none';
                }
            }
        });
    }

    setUserInfo(user_info) {
        this.user_info = user_info;

        this.text_logged_in_as = this.add.text(
            10, 10,
            'Logged in as ' + user_info.username,
            { font: '8pt Verdana', fill: '#FFFFFF' });
    }

    chatMsg(data) {
        this.chat_msgs_history.push(data.from + ': ' + data.msg);

        let chat_msgs = '';
        const start = this.chat_msgs_history.length - 10;
        const end = this.chat_msgs_history.length;

        for (let i = start; i < end; i++) {
            if (i >= 0) {
                chat_msgs += this.chat_msgs_history[i] + '\n';
            } else {
                chat_msgs += '\n';
            }
        }

        this.text_chat_msgs.text = chat_msgs;
    }
}
