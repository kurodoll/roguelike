const socket = io.connect();

$(() => {
    // ================================================================= Phaser
    const phaser_config = {
        type: Phaser.AUTO,
        width: '99vw',
        height: '99vh',
        scene: [ SceneLogin, SceneGUI, SceneGame ]
    };

    const game = new Phaser.Game(phaser_config);
    game.scene.start('login');

    socket.on('login_success', (user_info) => {
        game.scene.switch('login', 'gui');
        game.scene.start('game')

        game.scene.getScene('gui').setUserInfo(user_info);
    });

    socket.on('chat_msg', (data) => {
        game.scene.getScene('gui').chatMsg(data);
    });
});
