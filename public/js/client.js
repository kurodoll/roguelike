const socket = io.connect();

$(() => {
    // ================================================================= Phaser
    const phaser_config = {
        type: Phaser.AUTO,
        width: '100%',
        height: '100%',
        scene: [ SceneLogin, SceneGame ]
    };

    const game = new Phaser.Game(phaser_config);
    game.scene.start('login');

    socket.on('login_success', (data) => {
        game.scene.switch('login', 'game');
        game.scene.getScene('game').setUserInfo(data.user_info);
    });
});
