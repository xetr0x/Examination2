class DiceHand:

    def init(self, num_dice):
        self.dice_list = []
        for _ in range(num_dice):
            self.dice_list.append(Dice(6))

    def roll_all(self):
        for dice in self.dice_list:
            dice.roll()
      
    def get_values(self):
        return [dice.value for dice in self.dice_list]
