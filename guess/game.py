#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Guess the number I am thinking of."""

import random
import dice
import highscore
import keyboard

class Game:

    """the game class containing the game"""


    
    def __init__(self):
        """init the object"""   # TODO Loop where all points in a
        # given round are tracked and thhen added to archive at the end of it
        # Ex. add_scores(player1Score, Player2Score, Player3Score, Player4Score)
        self.highscore = highscore.Highscore().PLAYERS
        self.the_dice = dice.Dice()
        self.current_player = 1
        self.current_round = 1
        self.p1 = "player 1"
        self.p2 = "player 2"  # makes it possible to change name later
        self.p3 = "player 3"
        self.p4 = "player 4"
        self.playercount = 0  # counts amount of players
        self.players = {1: (self.p1, highscore.get("player 1")), 2: self.p2, 3: self.p3, 4: self.p4}
        self.player1 = self.highscore.player1
        self.player2 = self.highscore.player2
        if self.highscore.player3 is not None:
            self.player3 = self.highscore.player3
        else:
            self.player3 = None
        if self.highscore.player4 is not None:
            self.player4 = self.highscore.player4
        else:
            self.player4 = None

    def start_game(self, n=1):
        """starts the game"""
        diff = {1: 0, 2: 10, 3: 15, 4: 20}  # make it into diff file
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
        if self.playercount == 1 or 2:
            scores = highscore.Highscore(0, diff.get(n))
        elif self.playercount == 3:
            scores = highscore.Highscore(0, 0, 0)
        elif self.playercount == 4:
            scores = highscore.Highscore(0, 0, 0, 0)
        
        self.round()  # TODO looping round()
        print("test")
    

    
    def round(self):
        """collection of methods that make together a round"""
        while self.current_player == self.playercount:
            print(f"{self.players.get(self.current_player)} please press space to roll the dices!")
            keyboard.add_hotkey("space", self.the_dice.roll)

            keyboard.wait("space")

            result = self.the_dice.value
        print(result)
        # TODO updating the scores   (addscore method)
        # TODO keeping tabs on round number (method)
        # TODO clearing cmd with 'cls'
        # TODO space on press input way  (method for press)
        # TODO keep playing (method)
        # TODO keep track of which players turn it is
        # TODO A round is done when all of the players have done their turn

