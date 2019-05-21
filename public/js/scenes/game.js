class SceneGame extends Phaser.Scene {
    constructor() {
        super({ key: 'game' });
    }

    create() {
        ;
    }

    setUserInfo(user_info) {
        this.user_info = user_info;

        this.text_logged_in_as = this.add.text(
            10, 10,
            'Logged in as ' + user_info.username,
            { font: '8pt Verdana', fill: '#FFFFFF' });
    }
}
