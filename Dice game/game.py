#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Dice Game."""


class Game:
    
    def init(self):
        self.players = []
        self.current_player_index = 0
        self.high_scores = {}
        self.load_high_scores()

    def add_player(self, name):
        player = Player(name)
        self.players.append(player)

    def load_high_scores(self):
        # Load high scores from file or database
        pass

    def save_high_scores(self):
        # Save high scores to file or database
        pass

    def update_high_scores(self):
        for player in self.players:
            if player.name not in self.high_scores:
                self.high_scores[player.name] = {"games_played": 0, "total_score": 0}
            self.high_scores[player.name]["games_played"] += 1
            self.high_scores[player.name]["total_score"] += player.score
        self.save_high_scores()

    def show_high_scores(self):
        print("High Scores:")
        for name, stats in self.high_scores.items():
            games_played = stats["games_played"]
            total_score = stats["total_score"]
            avg_score = total_score / games_played
            print(f"{name}: Games played: {games_played}, Total score: {total_score}, Average score: {avg_score}")

    def get_current_player(self):
        return self.players[self.current_player_index]

    def next_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def play_game(self):
        # Reset player scores
        for player in self.players:
            player.reset_score()
        while True:
            current_player = self.get_current_player()
            print(f"It's {current_player.name}'s turn.")
            num_dice_input = input("How many dice do you want to roll? [1-6] ")# import random


# class Game:
#     """Example of dice class."""

#     low_number = 1
#     high_number = 100
#     the_number = None

#     def __init__(self):
#         """Init the object."""
#         random.seed()

#     def start(self):
#         """Start the game and randomize a new number."""
#         self.the_number = random.randint(self.low_number, self.high_number)

#     def cheat(self):
#         """Get the number."""
#         return self.the_number

#     def low(self):
#         """Get the lowest number possible."""
#         return self.low_number

#     def high(self):
#         """Get the highest number possible."""
#         return self.high_number

#     def guess(self, a_number):
#         """
#         Check it the guess is correct, higher or lower than the actual number.

#         Raise an exception if the number is out of range.
#         Raise an exception if the number is not an integer.
#         """
#         if not isinstance(a_number, int):
#             raise TypeError("The number should be an integer.")

#         if not self.low_number <= a_number <= self.high_number:
#             raise ValueError("The number is higher/lower than max/min value.")

#         msg = "Too Low"
#         if a_number == self.the_number:
#             msg = "Correct"
#         elif a_number > self.the_number:
#             msg = "Too High"

#         return msg
