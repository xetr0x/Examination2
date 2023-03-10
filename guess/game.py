#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Guess the number I am thinking of."""

import random
import dice
import highscore


class Game:

    """the game class containing the game"""


    
    def __init__(self):
        """init the object"""   # TODO Loop where all points in a
        # given round are tracked and thhen added to archive at the end of it
        # Ex. add_scores(player1Score, Player2Score, Player3Score, Player4Score)

    def start_game(self, n=1):
        """starts the game"""
        diff = {1: 0, 2: 10, 3: 15, 4: 20}
        while True:
            try:
                playercount = int(input("How many players? 1-4, if the number is 1, you will get an Npc"
                                        + "to play against "))
                if 1 <= playercount <= 4:
                    break
                else: 
                    print("invalid choice, only between 1-4!")
            except ValueError:
                print("invalid choice, please enter an number between 1 and 4")
        if playercount == 1 or 2:
            scores = highscore.Highscore(0, diff.get(n))
        elif playercount == 3:
            scores = highscore.Highscore(0, 0, 0)
        elif playercount == 4:
            scores = highscore.Highscore(0, 0, 0, 0)
        
        round() # TODO looping round()

    def round():
        """collection of methods that make together a round"""
        input("please press space to roll the dices!")
        # TODO Making alll players throw dices (roll method)
        # TODO updating the scores   (addscore method)
        # TODO keeping tabs on round number (method)
        # TODO clearing cmd with 'cls'
        # TODO space on press input way  (method for press)
        # TODO keep playing (method)

