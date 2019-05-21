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

    $(document).on('keydown', function(e) {        
        if (e.keyCode === 8) {
           e.preventDefault();

           if (game.scene.isActive('login')) {
               game.scene.getScene('login').specialChar(8)
           } else if (game.scene.isActive('gui')) {
            game.scene.getScene('gui').specialChar(8)
        }
         }
    });
});
