from random import randint
from collections import defaultdict

class Die:
    def __init__(self, sides):
        self.sides = sides

    def __repr__(self):
        return "{}-sided".format(self.sides)

    __str__ = __repr__

    def roll(self, n = 1):
        return [randint(1, self.sides) for _ in range(n)]
