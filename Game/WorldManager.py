from log import log
import json


class WorldManager:
    def __init__(self):
        self.levels = {}

        filename = 'Game/data/world/defined_levels.json'
        try:
            self.defined_levels = json.load(open(filename, 'r'))
            log('WorldManager', 'Loaded ' + filename)
        except IOError:
            log('WorldManager', 'Failed to open ' + filename, 'error')
            self.defined_levels = {}

    def defaultLevel(self):
        return 'test_level'

    def getLevel(self, level_title):
        if level_title not in self.levels.keys():
            self.loadLevel(level_title)

        if level_title in self.levels.keys():
            return self.levels[level_title]
        else:
            log('WorldManager', 'Couldn\'t load ' + level_title, 'error')

    def getLevelElement(self, level_title, element):
        if level_title not in self.levels.keys():
            self.loadLevel(level_title)

        if level_title in self.levels.keys():
            level = self.levels[level_title]

            if 'elements' in level.keys():
                if 'spawn' in level['elements'].keys():
                    return level['elements']['spawn']

            log('WorldManager', 'No element ' + element + ' in ' + level_title,
                'error')
        else:
            log('WorldManager', 'Couldn\'t load ' + level_title, 'error')

    def loadLevel(self, level_title):
        log('WorldManager', 'Loading level ' + level_title)

        if level_title in self.defined_levels.keys():
            filename = self.defined_levels[level_title]

            try:
                level_data = json.load(open(filename, 'r'))
            except IOError:
                log('WorldManager', 'Failed to open ' + filename, 'error')
                return

            self.levels[level_title] = level_data
            log('WorldManager', 'Loaded level ' + level_title)
