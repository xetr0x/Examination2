import unittest
from unittest.mock import patch
from dice import Dice


class TestDice(unittest.TestCase):

    def setUp(self):
        self.dice = Dice()

    """
    First test ensures that roll() method returns 2 integers.
    Checks whether the type of dice1 and dice2 are integers using assertIsInstance.
    """

    def test_roll_returns_integers(self):
        dice1, dice2 = self.dice.roll()
        self.assertIsInstance(dice1, int)
        self.assertIsInstance(dice2, int)

    """
    2nd test checks whether the numbers returned by roll() are in the range of 1 to 6. 
    We use a for loop to call the roll() method 100 times and check the range of both 
    dice values using assertGreaterEqual and assertLessEqual.
    """

    def test_roll_range(self):
        for i in range(100):
            dice1, dice2 = self.dice.roll()
            self.assertGreaterEqual(dice1, 1)
            self.assertLessEqual(dice1, 6)
            self.assertGreaterEqual(dice2, 1)
            self.assertLessEqual(dice2, 6)

    """
    3rd test checks whether the dicefaces() method prints the correct 
    visual representation of a dice when the input value is 1. 
    We use a patch decorator to mock the print() function and 
    check whether it is called with the expected string.
    """

    def test_dicefaces(self):
        with patch('builtins.print') as mock_print:
            self.dice.dicefaces(1)
            mock_print.assert_called_with(".-------.\n"
                                          "|       |\n"
                                          "|   O   |\n"
                                          "|       |\n"
                                          "'-------'")
    
    """
    4th test checks whether dicefaces() method raises a ValueError when the input value 
    is <1 or >6. We use assertRaises to check whether the method raises an exception
    for invalid input values.
    """

    def test_dicefaces_invalid_number(self):
        with self.assertRaises(ValueError):
            self.dice.dicefaces(0)
        with self.assertRaises(ValueError):
            self.dice.dicefaces(7)
    
    """
    5th test checks whether the dicefaces() method prints the visual representation
    of all numbers between 1 and 6. It uses the patch decorator to mock the print() function
    and checks whether it is called for all input values using assertCalled().
    """

    def test_dicefaces_all_numbers(self):
        with patch('builtins.print') as mock_print:
            for i in range(1, 7):
                self.dice.dicefaces(i)
                mock_print.assert_called()

    """6th test checks whether the roll() method returns different results when called
    multiple times. We use a set to store the unique results obtained by calling
     roll() method 100 times and check whether the length of the set is >1 using assertGreater."""

    def test_roll_different_results(self):
        results = set()
        for i in range(100):
            dice1, dice2 = self.dice.roll()
            results.add((dice1, dice2))
        self.assertGreater(len(results), 1)
    
    """
    7th test checks whether the average of the values returned by the roll() method
    is close to the expected value of 7. It calls the roll() method 1000 times, 
    stores the results in a list, calculates the average, and checks whether it is close
    to the expected value using assertAlmostEqual.
    """

    def test_roll_average(self):
        results = []
        for i in range(1000):
            dice1, dice2 = self.dice.roll()
            results.append(dice1 + dice2)
        average = sum(results) / len(results)
        self.assertAlmostEqual(average, 7, delta=1)

    """
    8th test checks whether an instance of the Dice class can be created using
    the __init__ method. We create a new instance of the Dice class and check
    whether its type is Dice using assertIsInstance.
    """

    def test_init(self):
        dice = Dice()
        self.assertIsInstance(dice, Dice)
    
    """
    9th test checks whether the roll() and dicefaces() methods can be called together 
    without any errors. We use the patch decorator to mock the print() function and check
    whether it is called twice using assertEqual.
    """

    def test_roll_and_dicefaces_together(self):
        with patch('builtins.print') as mock_print:
            dice1, dice2 = self.dice.roll()
            self.dice.dicefaces(dice1)
            self.dice.dicefaces(dice2)
            self.assertEqual(mock_print.call_count, 2)
    
    """
    10th test checks whether the output of the roll() and dicefaces() methods matche
    the expected output. We use the patch decorator to mock the print() function and check 
    whether the combined output of 2 methods matches the expected output using assertEqual.
    """

    def test_roll_and_dicefaces_output(self):
        with patch('builtins.print') as mock_print:
            dice1, dice2 = self.dice.roll()
            self.dice.dicefaces(dice1)
            self.dice.dicefaces(dice2)
            expected_output = (".-------.\n"
                               "|       |\n"
                               "|   O   |\n"
                               "|       |\n"
                               "'-------'\n"
                               ".-------.\n"
                               "|       |\n"
                               "|   O   |\n"
                               "|       |\n"
                               "'-------'\n")
            self.assertEqual(mock_print.call_args[0][0], expected_output)

    """
    Final test checks if the roll() method can handle a very large number (10^1000) 
    without crashing or causing any other unexpected behavior. 
    If this method is not properly secured against buffer overflow attacks,
    this test will fail and indicate a potential security vulnerability.
    """

    def test_roll_buffer_overflow(self):
        with patch('builtins.print') as mock_print:
            # Pass a very large number as argument to roll() method
            # to check if it can handle large inputs without crashing
            self.dice.roll(10**1000)
            mock_print.assert_not_called()


if __name__ == '__main__':
    unittest.main()
