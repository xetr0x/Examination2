#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Guess the number I am thinking of."""

import random
import dice
import highscore


class Game:

    """the game class containing the game"""
    lol = highscore.Highscore(0, 0, 0, 0)
    print(lol.add_scores(2,20,10,4))

    
    def __init__(self):
        """init the object"""   # TODO Loop where all points in a
        # given round are tracked and thhen added to archive at the end of it
        # Ex. add_scores(player1Score, Player2Score, Player3Score, Player4Score)


        
        





    # """Example of dice class."""

    # low_number = 1
    # high_number = 100
    # the_number = None

    # def __init__(self):
    #     """Init the object."""
    #     random.seed()

    # def start(self):
    #     """Start the game and randomize a new number."""
    #     self.the_number = random.randint(self.low_number, self.high_number)

    # def cheat(self):
    #     """Get the number."""
    #     return self.the_number

    # def low(self):
    #     """Get the lowest number possible."""
    #     return self.low_number

    # def high(self):
    #     """Get the highest number possible."""
    #     return self.high_number

    # def guess(self, a_number):
    #     """
    #     Check it the guess is correct, higher or lower than the actual number.

    #     Raise an exception if the number is out of range.
    #     Raise an exception if the number is not an integer.
    #     """
    #     if not isinstance(a_number, int):
    #         raise TypeError("The number should be an integer.")

    #     if not self.low_number <= a_number <= self.high_number:
    #         raise ValueError("The number is higher/lower than max/min value.")

    #     msg = "Too Low"
    #     if a_number == self.the_number:
    #         msg = "Correct"
    #     elif a_number > self.the_number:
    #         msg = "Too High"

    #     return msg
