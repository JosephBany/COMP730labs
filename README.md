
# Riddle Game (Python OOP Project)

1. Design Phase

In the design phase, we plan how to structure the program using OOP concepts.
We need:
A Riddle class → represents a riddle with its question and answer.
A RiddleGame class → manages riddles, asks them, and checks answers.


# Project Structure
```
riddle_game/
│── riddles.py        # Main game logic
│── test_riddles.py   # Unit tests
│── README.md         # Documentation
```

2. Implementation Phase (Python OOP Code)

python3 riddles.py

This runs the program interactively.
The program prints riddles and waits for you to type answers.
It gives instant feedback, like:

✅ Correct!

❌ Wrong! The correct answer is …
This is what a user would see when actually playing the game

3. Testing Phase

Example test run in terminal:

Riddle: What is harder to catch the faster you run?
Your answer: your breath
✅ Correct!

Riddle: What has many keys but can’t open a single lock?
Your answer: keyboard
❌ Wrong! The correct answer is: Piano

The program works: it checks answers, accepts input, and gives feedback.


4. Documentation Phase

Program Purpose:

This Python program uses Object-Oriented Programming (OOP) to create a simple Riddle Game. Each riddle has a question and an answer, stored in a Riddle object. The RiddleGame class manages multiple riddles and interacts with the user.

Key OOP Concepts Used:

Abstraction: Only necessary details (question, answer) are exposed.

Encapsulation: Data (question, answer) is bundled with behavior (check_answer).

Modularity: Each class has a single responsibility.

Reusability: New riddles can easily be added.

# How to Run the Game
```bash
python3 riddles.py
```

---

# Running Unit Tests
```bash
python3 -m unittest test_riddles.py
```

---

# Example Riddles
1. What is harder to catch the faster you run? → *Your breath*  
2. What has many keys but can’t open a single lock? → *Piano*  
