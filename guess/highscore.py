#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio

class Highscore():
    """class for keeping track of highscore"""

    def __init__(self, player1, player2, player3=None, player4=None):
        """init the objects creating highscores"""
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3
        self.player4 = player4
        # Makes the accessable inside class methods
        Highscore.PLAYERS = {"Player 1": self.player1,
                             "Player 2": self.player2,
                             "Player 3": self.player3,
                             "Player 4": self.player4}
        # player variables works as medium for the points

    def add_scores(self, score1, score2, score3=None, score4=None):
        # will be used as refresh
        """adds and sorts scores"""
        # Player 3 - 4 will always exist but will be as none if not played
        # This way we can make them invinsible if not played, but still exist
        player1 = ("Player 1", Highscore.PLAYERS.get("Player 1") + score1)
        player2 = ("Player 2", Highscore.PLAYERS.get("Player 2") + score2)
        if score3 and Highscore.PLAYERS.get("Player 3", None) is not None:
            # if both are none
            # then it means that the player is non existent!
            player3 = ("Player 3", Highscore.PLAYERS.get("Player 3") + score3)
        else:
            player3 = None
        if score4 and Highscore.PLAYERS.get("player 4", None) is not None:
            player4 = ("Player 4", Highscore.PLAYERS.get("Player 4", None) +
                       score4)
        else:
            player4 = None
            # makes player none existent if nonexistent
        # implementation of simple bubble sort with tupples
        thelist = list(filter(None, [player1, player2, player3, player4]))
        # filtering None values
        number = len(thelist)
        for i in range(number-1):
            for j in range(0, number-i-1):
                if thelist[j][1] > thelist[j+1][1]:
                    thelist[j], thelist[j+1] = thelist[j+1], thelist[j]
        # await asyncio.sleep(1) to refresh the code every sec
        return thelist   # Returns sorted list of the players

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
