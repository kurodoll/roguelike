from . import WorldManager


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
            'present_level': self.WorldManager.defaultLevel()
        }

    def getLevel(self, level_title):
        return self.WorldManager.getLevel(level_title)
