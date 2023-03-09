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
        else: 
            player3 = -1
        if player4 is not None:
            self.player4 = player4
        else:
            player4 = -1
        players = {"Player 1": player1, "Player 2": player2,
                   "Player 3": player3, "Player 4": player4}
        
    def add_scores(self, players):      # will be used as refresh
        """adds and sorts scores"""
        # Player 3 - 4 will always exist but will be as none if not played
        # This way we can make them invinsible if not played, but still exist
        player1 = ("Player 1", players.get("Player 1"))
        player2 = ("Player 2", players.get("Player 2"))
        player3 = ("Player 3", players.get("Player 3"))
        player4 = ("Player 4", players.get("Player 4")) # TODO finding way to have as tuples and sorted afterwards!

        thelist = [player1, player2, player3, player4]
        n = len(thelist)
        for i in 4:
        # Last i elements are already sorted
            for j in range(0, n-i-1):
                # Swap if the element found is greater than the next element
                if thelist[j] > thelist[j+1]:
                thelist[j], thelist[j+1] = thelist[j+1], thelist[j]


        


        

        



    def get_high_scores(self):
        """shows the highscore table"""
        print("--------------------------------------------------")
        print()
        print()
        print()
