class SceneGame extends Phaser.Scene {
    constructor() {
        super({ key: 'game' });
    }

    preload() {
        this.load.image('.', '/graphics/tile/ground.png')
        this.load.image('player', '/graphics/sprite/player.png')
    }

    create() {
        const movement_keys = [ '1', '2', '3', '4', '6', '7', '8', '9' ];

        this.input.keyboard.on('keydown', (e) => {
            if (movement_keys.indexOf(e.key) > -1) {
                socket.emit('action', {
                    'action': 'move',
                    'dir': e.key });
            }
        });
    }

    setLevel(level) {
        this.level = level;

        this.cameras.main.centerOn(
            (level.level.width * level.level.tile_width) / 2,
            (level.level.height * level.level.tile_height) / 2
        );

        this.cameras.main.setZoom(level.level.camera_zoom);

        for (let x = 0; x < level.level.width; x++) {
            for (let y = 0; y < level.level.height; y++) {
                this.add.image(
                    x * parseInt(level.level.tile_width),
                    y * parseInt(level.level.tile_height),
                    level.level.tiles[x * level.level.width + y]
                ).setOrigin(0, 0);
            }    
        }
    }

    setPlayerInfo(player_info) {
        this.player_info = player_info;

        if (!this.player_sprite) {
            this.player_sprite = this.add.sprite(
                player_info.position.x * parseInt(this.level.level.tile_width),
                player_info.position.y * parseInt(this.level.level.tile_height),
                'player'
            ).setOrigin(0, 0);
        } else {
            this.player_sprite.x = player_info.position.x * parseInt(this.level.level.tile_width);
            this.player_sprite.y = player_info.position.y * parseInt(this.level.level.tile_height);
        }
    }
}
