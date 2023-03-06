import random


class Intelligence:
    def init(self, level):
        self.level = level

    def should_roll_again(self, score):
        if self.level == "dumb":
            return random.randint(0, 1)
        elif self.level == "smart":
            return score < 15
        elif self.level == "genius":
            return score < 20
        else:
            raise ValueError("Invalid intelligence level")
