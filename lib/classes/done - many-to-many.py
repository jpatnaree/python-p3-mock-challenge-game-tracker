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
            if isinstance(new_title, str) and len(new_title) > 0 : #alternative new_player != "":
                self._title = new_title
            else: 
                raise Exception('')

    def results(self):
        return [ r for r in Result.all if r.game == self]

    def players(self):
        return list(set([r.player for r in Result.all if r.game == self]))

    def average_score(self, player):

        player_score = [r.score for r in Result.all if r.player == player and r.game == self]
        return sum(player_score) / len(player_score) if player_score else 0
        #alternative method
        # return mean(player_score) if len(player_score) > 0 else 0



class Player:

    all = []

    def __init__(self, username):
        self.username = username
        Player.all.append(self)

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, new_user):
        if isinstance(new_user, str) and (2 <= len(new_user) <= 16):
            self._username = new_user
        else:
            print('')

    def results(self):
        return [ r for r in Result.all if r.player == self]

    def games_played(self):
        return list(set([ r.game for r in Result.all if r.player == self]))

    def played_game(self, game):
        
        return True if game in self.games_played() else False
        #Alternative
        #return game in self.games_played() # already return True or False

    def num_times_played(self, game):
        
        return [ r.game for r in Result.all if r.player == self].count(game)
        #Alternative
        # return len([ r.game for r in Result.all if r.player == self and r.game == game])

    @classmethod
    def highest_scored(game):
        pass

class Result:

    all = []


    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self._score = score
        Result.all.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, new_score):
        if not hasattr(self, '_score'):
            if isinstance(new_score, int) and (1<= new_score <= 5000):
                self._score = new_score
            else:
                raise Exception('')
        
    