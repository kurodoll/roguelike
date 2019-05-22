class SceneGame extends Phaser.Scene {
    constructor() {
        super({ key: 'game' });
    }

    preload() {
        this.load.image('.', '/graphics/tile/ground.png')
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
}
