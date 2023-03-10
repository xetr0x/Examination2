import unittest
from highscore import Highscore


class TestHighscore(unittest.TestCase):
    """
    A class for unit testing the Highscore class methods.
    """

    def setUp(self):
        """
        Initializes the highscore instance to test methods on.
        """
        self.highscore = Highscore(0, 0)

    def test_add_scores(self):
        """
        Tests adding scores for multiple players.
        """
        # Test adding scores for two players
        result = self.highscore.add_scores(10, 20)
        self.assertEqual(result, [('Player 1', 10), ('Player 2', 20)])

        # Test adding scores for three players
        self.highscore = Highscore(0, 0, 0)
        result = self.highscore.add_scores(10, 20, 30)
        self.assertEqual(result, [('Player 1', 10), ('Player 2', 20), ('Player 3', 30)])

        # Test adding scores for four players
        self.highscore = Highscore(0, 0, 0, 0)
        result = self.highscore.add_scores(10, 20, 30, 40)
        self.assertEqual(result, [('Player 1', 10), ('Player 2', 20), ('Player 3', 30), ('Player 4', 40)])

    def test_get_high_scores(self):
        """
        Tests getting high scores for multiple players.
        """
        # Test displaying high scores for two players
        self.highscore = Highscore(10, 20)
        result = self.highscore.get_high_scores(self.highscore.add_scores(10, 20))
        expected_result = "------------------------------------------\n      Name                 Highscore      \n-------------------------------------------\nPlayer 2: 20\n------------------------------------------\nPlayer 1: 10\n------------------------------------------"
        self.assertEqual(result, expected_result)

        # Test displaying high scores for three players
        self.highscore = Highscore(10, 20, 30)
        result = self.highscore.get_high_scores(self.highscore.add_scores(10, 20, 30))
        expected_result = "------------------------------------------\n      Name                 Highscore      \n-------------------------------------------\nPlayer 3: 30\n------------------------------------------\nPlayer 2: 20\n------------------------------------------\nPlayer 1: 10\n------------------------------------------"
        self.assertEqual(result, expected_result)

        # Test displaying high scores for four players
        self.highscore = Highscore(10, 20, 30, 40)
        result = self.highscore.get_high_scores(self.highscore.add_scores(10, 20, 30, 40))
        expected_result = "------------------------------------------\n      Name                 Highscore      \n-------------------------------------------\nPlayer 4: 40\n------------------------------------------\nPlayer 3: 30\n------------------------------------------\nPlayer 2: 20\n------------------------------------------\nPlayer 1: 10\n------------------------------------------"
        self.assertEqual(result, expected_result)

    def test_add_scores_security(self):
        """
        Tests adding scores with negative or string values.
        """
        # Test adding a negative score.
        with self.assertRaises(ValueError):
            self.highscore.add_scores(-10)

        # Test adding a string score.
        with self.assertRaises(TypeError):
            self.highscore.add_scores('test')

    def test_get_high_scores_security(self):
        """
        Tests getting high scores with invalid input.
        """
        # Test getting high scores with invalid input.
        with self.assertRaises(TypeError):
            self.highscore.get_high_scores('invalid')


if __name__ == '__main__':
    unittest.main()



