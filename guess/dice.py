#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random


class Dice():
    """Everything thats tied to Dices"""
    def __init__(self):
        """init object"""
        self.value = None

    def roll(self):
        """rolls 2 dices and returns their number"""
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        self.dicefaces(dice1)
        self.dicefaces(dice2)
        self.value = (dice1, dice2)
        return self.value

    def dicefaces(self, number):
        """Different faces of dice for visual effect"""
        def one():
            """1"""
            print(".-------." + '\n'
                  "|       |" '\n'
                  "|   O   |" '\n'
                  "|       |" '\n'
                  "'-------'")

        def two():
            """2"""
            print(".-------." + '\n'
                  "| O     |" '\n'
                  "|       |" '\n'
                  "|     O |" '\n'
                  "'-------'")

        def three():
            """3"""

            print(".-------." + '\n'
                  "| O     |" '\n'
                  "|   O   |" '\n'
                  "|     O |" '\n'
                  "'-------'")

        def four():
            """4"""
            print(".-------." + '\n'
                  "| O   O |" '\n'
                  "|       |" '\n'
                  "| O   O |" '\n'
                  "'-------'")

        def five():
            """5"""
            print(".-------." + '\n'
                  "| O   O |" '\n'
                  "|   O   |" '\n'
                  "| O   O |" '\n'
                  "'-------'")

        def six():
            """6"""
            print(".-------." + '\n'
                  "| O   O |" '\n'
                  "| O   O |" '\n'
                  "| O   O |" '\n'
                  "'-------'")
            
        if number == 1:
            one()
        elif number == 2:
            two()
        elif number == 3:
            three()
        elif number == 4:
            four()
        elif number == 5:
            five()
        elif number == 6:
            six()
                    
