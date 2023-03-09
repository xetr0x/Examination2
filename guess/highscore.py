#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Highscore():
    """class for keeping track of highscore"""

    def __init__(self, player1, player2, player3=None, player4=None):
        """init the objects creating highscores"""
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3
        self.player4 = player4
        global players
        players = {"Player 1": self.player1, "Player 2": self.player2,
                   "Player 3": self.player3, "Player 4": self.player4}
        # player variables works as medium for the points
    def add_scores(self, players, points, player):
        playerpoints = players.get(player)
        self.player 
    
    def sort(self):      # will be used as refresh
        """adds and sorts scores"""
        # Player 3 - 4 will always exist but will be as none if not played
        # This way we can make them invinsible if not played, but still exist
        # player1 = ("Player 1", players.get("Player 1"))
        # player2 = ("Player 2", players.get("Player 2"))
        # player3 = ("Player 3", players.get("Player 3", None))
        # player4 = ("Player 4", players.get("Player 4", None))
        # implementation of simple bubble sort
        thelist = list(filter(None, [self.player1, self.player2, self.player3, self.player4])) # filtering None values
        n = len(thelist)
        for i in 4:
            # Last i elements are already sorted
            for j in range(0, n-i-1):
                # Swap if the element found is greater than the next element
                if thelist[j] > thelist[j+1]:
                    thelist[j][1], thelist[j+1][1] = thelist[j+1][1],
                    thelist[j][1]

        return thelist   # returns sorted list of the players
    


    def get_high_scores(self, thelist):
        """shows the highscore table"""
        print("------------------------------------------")
        print("      Name                 Highscore      ")
        print("-------------------------------------------")
        print(f'{thelist[0][0]}{thelist[0][1]}')
        print("------------------------------------------")
        print(f'{thelist[1][0]}{thelist[1][1]}')
        print("------------------------------------------")
        if len(thelist) == 3:
            print(f'{thelist[2][0]}{thelist[2][1]}')
            print("------------------------------------------")
            if len(thelist) == 4:
                print(f'{thelist[3][0]}{thelist[3][1]}')
                print("------------------------------------------")
