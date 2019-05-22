from . import WorldManager
from log import log


class Manager:
    def __init__(self):
        self.WorldManager = WorldManager.WorldManager()
        self.players = {}

    def getPlayerLevel(self, username):
        if username not in self.players.keys():
            self.addNewPlayer(username)

        return self.players[username]['present_level']

    def addNewPlayer(self, username):
        self.players[username] = {
            'present_level': self.WorldManager.defaultLevel(),
            'position': self.WorldManager.getLevelElement(
                self.WorldManager.defaultLevel(),
                'spawn'
            )
        }

    def getPlayerInfo(self, username):
        if username in self.players.keys():
            return self.players[username]
        else:
            log('Manager', 'No player ' + username, 'error')

    def getLevel(self, level_title):
        return self.WorldManager.getLevel(level_title)

    def playerAction(self, player_username, action):
        if player_username not in self.players.keys():
            log('Manager', 'Got action for non-existant player', 'warning')

        if action['action'] == 'move':
            if 'dir' in action.keys() and action['dir'] == '1':
                self.players[player_username]['position']['x'] -= 1
                self.players[player_username]['position']['y'] += 1
            elif 'dir' in action.keys() and action['dir'] == '2':
                self.players[player_username]['position']['y'] += 1
            elif 'dir' in action.keys() and action['dir'] == '3':
                self.players[player_username]['position']['x'] += 1
                self.players[player_username]['position']['y'] += 1
            elif 'dir' in action.keys() and action['dir'] == '4':
                self.players[player_username]['position']['x'] -= 1
            elif 'dir' in action.keys() and action['dir'] == '6':
                self.players[player_username]['position']['x'] += 1
            elif 'dir' in action.keys() and action['dir'] == '7':
                self.players[player_username]['position']['x'] -= 1
                self.players[player_username]['position']['y'] -= 1
            elif 'dir' in action.keys() and action['dir'] == '8':
                self.players[player_username]['position']['y'] -= 1
            elif 'dir' in action.keys() and action['dir'] == '9':
                self.players[player_username]['position']['x'] += 1
                self.players[player_username]['position']['y'] -= 1

        return 'send player info'
