import unittest
from unittest.mock import patch
from io import StringIO
from game import Game


class TestGame(unittest.TestCase):
    """Test the Game class"""

    def setUp(self):
        """Set up a new Game instance for each test method"""
        self.game = Game()

    def test_start_game_with_one_player(self):
        """Test that start_game method works with one player"""
        with patch('builtins.input', return_value='1'):
            # Set up a StringIO object to simulate user input
            expected_output = 'player 1 please press space to roll the dices!\n'
            with patch('sys.stdout', new=StringIO()) as fake_out:
                self.game.start_game()
                self.assertEqual(fake_out.getvalue(), expected_output)

    def test_start_game_with_two_players(self):
        """Test that start_game method works with two players"""
        with patch('builtins.input', return_value='2'):
            # Set up a StringIO object to simulate user input
            expected_output = 'player 1 please press space to roll the dices!\n'
            with patch('sys.stdout', new=StringIO()) as fake_out:
                self.game.start_game()
                self.assertEqual(fake_out.getvalue(), expected_output)

    def test_start_game_with_three_players(self):
        """Test that start_game method works with three players"""
        with patch('builtins.input', return_value='3'):
            # Set up a StringIO object to simulate user input
            expected_output = 'player 1 please press space to roll the dices!\n'
            with patch('sys.stdout', new=StringIO()) as fake_out:
                self.game.start_game()
                self.assertEqual(fake_out.getvalue(), expected_output)

    def test_start_game_with_four_players(self):
        """Test that start_game method works with four players"""
        with patch('builtins.input', return_value='4'):
            # Set up a StringIO object to simulate user input
            expected_output = 'player 1 please press space to roll the dices!\n'
            with patch('sys.stdout', new=StringIO()) as fake_out:
                self.game.start_game()
                self.assertEqual(fake_out.getvalue(), expected_output)

    def test_round(self):
        """Test that round method works"""
        # Set up a StringIO object to simulate user input
        with patch('builtins.input', return_value='1'):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                self.game.round()
                # Check that result of the_dice.roll is printed
                self.assertIn("Result:", fake_out.getvalue())
    
    def test_highscore_type(self):
        """Test that the highscore attribute is a dictionary"""
        self.assertIsInstance(self.game.highscore, dict)

    def test_dice_roll(self):
        """Test that the_dice attribute returns a number between 1 and 6"""
        result = self.game.the_dice.roll()
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 6)

    def test_players_type(self):
        """Test that the players attribute is a dictionary"""
        self.assertIsInstance(self.game.players, dict)

    def test_current_player(self):
        """Test that the current_player attribute is an integer"""
        self.assertIsInstance(self.game.current_player, int)

    def test_current_round(self):
        """Test that the current_round attribute is an integer"""
        self.assertIsInstance(self.game.current_round, int)


if __name__ == '__main__':
    unittest.main()



if __name__ == "__main__":
    unittest.main()
