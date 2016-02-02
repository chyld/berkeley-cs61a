class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def __repr__(self):
        return "Player: {}; Score: {}".format(self.name, self.score)

    __str__ = __repr__

    def largest_digit(self):
        digits = self.score % 100
        return max(digits // 10, digits % 10)
