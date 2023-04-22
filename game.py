class GamesA:
    def __init__(self):
        pass


class GamesB:
    def __init__(self):
        pass
  
#array used to test data parsing
class GamesTesting:
    def __init__(self):
        self.game_list = [] 
    def add_game(self, game):
        self.game_list.append(game)


class Game:
    def __init__(self, title, platform = '', metascore = 0, userscore = 0, genre = '', date = ''):
        self.title = title
        self.platform = platform
        self.metascore = metascore
        self.userscore = userscore
        self.genre = genre
        self.date = date
