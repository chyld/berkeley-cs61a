from functools import reduce
from die import Die

class Game:
    def __init__(self, p1, p2):
        self.players = [p1, p2]
        self.goal = 100
        self.turn = -1

    def play(self):
        while self.players[0].score < self.goal and self.players[1].score < self.goal:
            self.cycle_players();
            faces = self.die_size()
            attempts = self.strategy()
            score = self.go(faces, attempts)
            self.active_player.score += score
            self.swine_swap_rule()

    def cycle_players(self):
        self.turn += 1

    @property
    def active_player(self):
        return self.players[self.turn % 2]

    @property
    def next_player(self):
        return self.players[(self.turn + 1) % 2]

    def go(self, sides, tries):
        if tries == 0:
            return next_player.largest_digit() + 1

        rolls = Die(sides).roll(tries)
        return sum(rolls) if 1 not in rolls else 1

    def die_size(self):
        total = reduce(lambda acc, player: acc + player.score, self.players, 0)
        return 4 if total % 7 == 0 else 6

    def strategy(self):
        return 5

    def swine_swap_rule(self):
        x, y = [p.score for p in self.players]
        if x * 2 == y or x // 2 == y:
            temp = self.active_player.score
            self.active_player.score = self.next_player.score
            self.next_player.score = temp
