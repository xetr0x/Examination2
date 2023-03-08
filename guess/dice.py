#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random


class Dice():
    """Everything thats tied to Dices"""
    def __init__(self):
        """init object"""

    def roll(self):
        """rolls 2 dices and returns their number"""
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        return dice1 and dice2
        
    def dicefaces(self, number):
        """Different faces of dice for visual effect"""
        
        def one():
            """1"""
            print(".-------." + '\n'
                  "|       |" '\n'
                  "|   O   |" '\n'
                  "|       |" '\n'
                  "'-------'")

        def two(self):
            """2"""
            print(".-------." + '\n'
                  "| O     |" '\n'
                  "|       |" '\n'
                  "|     O |" '\n'
                  "'-------'")

        def three(self):
            """3"""

            print(".-------." + '\n'
                  "| O     |" '\n'
                  "|   O   |" '\n'
                  "|     O |" '\n'
                  "'-------'")

        def four(self):
            """4"""
            print(".-------." + '\n'
                  "| O   O |" '\n'
                  "|       |" '\n'
                  "| O   O |" '\n'
                  "'-------'")

        def five(self):
            """5"""
            print(".-------." + '\n'
                  "| O   O |" '\n'
                  "|   O   |" '\n'
                  "| O   O |" '\n'
                  "'-------'")

        def six(self):
            """6"""
            print(".-------." + '\n'
                  "| O   O |" '\n'
                  "| O   O |" '\n'
                  "| O   O |" '\n'
                  "'-------'")
