from random import randint
from collections import defaultdict

class Die:
    def __init__(self, sides):
        if type(sides) is not int:
            raise TypeError('Sides should be an int')
        if sides < 1 or sides > 20:
            raise ValueError('Only 1 to 20 sided die allowed')
        self.sides = sides
        self._rolls = []

    def __repr__(self):
        return "{}-sided".format(self.sides)

    __str__ = __repr__

    def roll(self):
        r = randint(1, self.sides)
        self.rolls.append(r)
        return r

    @property
    def rolls(self):
        return self._rolls

    def histogram(self):
        h = defaultdict(lambda: 0)
        for roll in self._rolls:
            h[roll] += 1
        for k, v in h.items():
            print("{} -> {}".format(k, v))
