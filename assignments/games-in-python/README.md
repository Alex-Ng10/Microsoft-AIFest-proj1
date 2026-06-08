
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic Hangman word-guessing game to practice string manipulation, loops, conditionals, and basic user input handling in Python.

## 🧭 Prerequisites

- Basic Python (variables, loops, conditionals, functions)
- Python 3.8+ installed

## ⚙️ Setup

1. Open the assignment folder.
2. Run the starter file with:

```bash
python3 starter-code.py
```

## 📝 Tasks

### 🛠️ Build the Hangman Game

#### Description
Create a console-based Hangman game where the player guesses letters to reveal a hidden word before running out of attempts.

#### Requirements
The completed program should:

- Randomly select a word from a predefined list.
- Display the current word progress using underscores for unknown letters (e.g., `_ a _ _ m a n`).
- Accept single-letter guesses (case-insensitive) and update the displayed progress.
- Track and display the number of incorrect attempts remaining.
- Prevent repeated penalty for the same incorrect guess.
- End the game when the word is fully guessed (win) or attempts reach zero (loss).
- Print a clear win or lose message and reveal the word at the end.

#### Example

```
Word: _ a _ _ m a n
Guesses remaining: 5
Enter a letter: g
Correct! Word: g a _ _ m a n
```

## 📤 Submission

- Modify and submit `starter-code.py` with your solution in the same folder.
- Include any additional modules you create.

## ✅ Grading Criteria

- Program runs without crashing: 40%
- Correct game logic and win/lose behavior: 40%
- Code clarity and comments: 20%

## 🔗 Resources

- Python `random` module documentation: https://docs.python.org/3/library/random.html

Good luck — ask for a hint if you get stuck!
