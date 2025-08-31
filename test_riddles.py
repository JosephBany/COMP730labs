"""
test_riddles.py
---------------
Unit tests for riddles.py using Python's unittest framework.
"""

import unittest
from riddles import Riddle, RiddleGame

class TestRiddle(unittest.TestCase):
    """Unit tests for the Riddle class."""

    def test_check_answer_correct(self):
        r = Riddle("What has many keys but can’t open a single lock?", "Piano")
        self.assertTrue(r.check_answer("piano"))

    def test_check_answer_incorrect(self):
        r = Riddle("What is harder to catch the faster you run?", "Your breath")
        self.assertFalse(r.check_answer("time"))


class TestRiddleGame(unittest.TestCase):
    """Unit tests for the RiddleGame class."""

    def test_add_riddle(self):
        game = RiddleGame()
        r = Riddle("What has many keys?", "Piano")
        game.add_riddle(r)
        self.assertEqual(len(game.riddles), 1)
        self.assertEqual(game.riddles[0].answer, "Piano")


if __name__ == "__main__":
    unittest.main()
