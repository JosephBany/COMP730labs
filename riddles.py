"""
riddles.py
----------
This module implements a simple Riddle Game using Object-Oriented Programming (OOP).
It contains two classes:
    - Riddle: represents a single riddle with a question and an answer
    - RiddleGame: manages multiple riddles, asks them, and checks answers
"""

class Riddle:
    
    ## Represents a single riddle with a question and its correct answer.
    

    def __init__(self, question, answer):
        """
        Initialize a riddle with a question and answer.

        Args:
            question (str): The riddle's question.
            answer (str): The correct answer to the riddle.
        """
        self.question = question
        self.answer = answer

    def check_answer(self, user_answer):
        """
        Check if the provided answer matches the correct answer.

        Args:
            user_answer (str): The user's guess.

        Returns:
            bool: True if the answer is correct, False otherwise.
        """
        return user_answer.strip().lower() == self.answer.lower()


class RiddleGame:
    
   # A game that manages multiple riddles and interacts with the user.
    
    def __init__(self):
        """Initialize the RiddleGame with an empty list of riddles."""
        self.riddles = []

    def add_riddle(self, riddle):
        """
        Add a new riddle to the game.

        Args:
            riddle (Riddle): The riddle to add.
        """
        self.riddles.append(riddle)

    def play(self):
        
        # Play the game by asking each riddle and checking the user's answer.
        
        for riddle in self.riddles:
            print("\nRiddle: " + riddle.question)
            user_answer = input("Your answer: ")
            if riddle.check_answer(user_answer):
                print("✅ Correct!")
            else:
                print(f"❌ Wrong! The correct answer is: {riddle.answer}")


if __name__ == "__main__":
    # Example riddles
    r1 = Riddle("What is harder to catch the faster you run?", "Your breath")
    r2 = Riddle("What has many keys but can’t open a single lock?", "Piano")

    # Create game
    game = RiddleGame()
    game.add_riddle(r1)
    game.add_riddle(r2)

    # Start the game
    game.play()
