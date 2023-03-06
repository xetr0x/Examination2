class Player:

    def init(self, name):
        self.name = name
        self.score = 0

    def add_score(self, score):
        self.score += score

    def reset_score(self):
        self.score = 0
