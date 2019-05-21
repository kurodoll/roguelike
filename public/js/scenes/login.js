class SceneLogin extends Phaser.Scene {
    constructor() {
        super({ key: 'login' });
    }

    create() {
        let entering = 'login';

        this.text_username = this.add.text(
            10, 10,
            'Username?',
            { font: '8pt Verdana', fill: '#FFFFFF' })

        this.text_username_entry = this.add.text(
            100, 10,
            '',
            { font: '8pt Verdana', fill: '#FFFFFF' })

        this.text_password = this.add.text(
            10, 30,
            'Password?',
            { font: '8pt Verdana', fill: '#FFFFFF' })

        this.text_password_entry = this.add.text(
            100, 30,
            '',
            { font: '8pt Verdana', fill: '#FFFFFF' })

        this.input.keyboard.on('keydown', (key) => {
            if (key.keyCode >= 65 && key.keyCode <= 90) {
                if (entering == 'login') {
                    this.text_username_entry.text += key.key;
                } else {
                    this.text_password_entry.text += key.key;
                }
            } else if (key.keyCode == 13) {
                if (entering == 'login') {
                    entering = 'password';
                } else {
                    socket.emit('login', {
                        username: this.text_username_entry.text,
                        password: this.text_password_entry.text
                    });
                }
            }
        });
    }
}
