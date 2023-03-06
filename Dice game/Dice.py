import random


class Dice:

    def init(self, num_sides):
        self.num_sides = num_sides
        self.value = None

    def roll(self):
        self.value = random.randint(1, self.num_sides)
