#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Highscore():
    """class for keeping track of highscore"""

    def __init__(self, player1, player2, player3, player4):
        """init the objects creating highscores"""
        self.player1 = player1
        self.player2 = player2
        if player3 is not None:
            self.player3 = player3  # if player 3 and 4 doesnt exist
        if player4 is not None:
            self.player4 = player4
        players = {"Player 1": player1, "Player 2": player2,
                   "Player 3": player3, "Player 4": player4}
        
    def add_scores(self, players):
        """adds and sorts scores"""
        try:
            players
    def show_player_score(self, players):
        try: 
            pl

    def get_high_scores(self):
        """shows the highscore table"""
        print("--------------------------------------------------")
        print()
        print()
        print()
