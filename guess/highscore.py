#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Highscore():
    """class for keeping track of highscore"""

    def __init__(self, player1, player2, player3, player4):
        """init the objects"""
        self.player1 = player1
        self.player2 = player2
        if player3 is not None:
            self.player3 = player3  # if player 3 and 4 doesnt exist
        if player4 is not None:
            self.player4 = player4

    def add_scores(self, player1, player2, player3, player4):



    def get_high_scores():
        print("--------------------------------------------------")
        print()
        print()
        print()