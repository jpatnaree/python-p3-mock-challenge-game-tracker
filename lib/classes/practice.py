from statistics import mean
class Game:

    all = []

    def __init__(self, title):
        self.title = title
        Game.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if not hasattr(self, '_title'):
            if isinstance(new_title, str) and len(new_title) > 0:
                self._title = new_title
            else:
                print('must be string')
        else:
            print('title cannot be changed')

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list(set([result.player for result in Result.all if result.game == self]))

    def average_score(self, player):
        scores = [result.score for result in Result.all if result.game == self and result.player == player]
        return sum(scores) / len(scores) if scores else 0
    #   return mean(scores)

class Player:

    all = []

    def __init__(self, username):
        self.username = username
        Player.all.append(self)

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, new_username):
        if isinstance(new_username, str) and 2 <= len(new_username) <= 16:
            self._username = new_username
        else:
            print('must be a string')


    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return list(set([result.game for result in Result.all if result.player == self]))

    def played_game(self, game):
        return True if game in self.games_played() else False

    def num_times_played(self, game):
        return [result.game for result in Result.all if result.player == self].count(game)

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

@property
def score(self):
    return self._score

@score.setter
def score(self, new_score):
    if not hasattr(self, '_score'):
        if isinstance(new_score, int) and (1 <= (new_score) <= 5000):
            self._score = new_score
        else:
            raise Exception('int please')
