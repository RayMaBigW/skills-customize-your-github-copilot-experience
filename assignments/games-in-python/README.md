# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a Hangman game in Python to practice strings, loops, conditionals, and user input. The player will guess a randomly selected word before running out of incorrect guesses.

## 📝 Tasks

### 🛠️ Set Up the Game and Process Guesses

#### Description
Complete the starter code to select a secret word and let the player guess its letters one at a time.

#### Requirements
Completed program should:

- Randomly select one word from the provided `words` list.
- Display unguessed letters as underscores and reveal correctly guessed letters in their positions.
- Accept a letter guess from the player and track letters that have already been guessed.
- Update and display the word's progress after each guess.

### 🛠️ Track Attempts and Finish the Game

#### Description
Add the attempt limit and win-or-lose conditions so the game ends when the player guesses the word or runs out of incorrect guesses.

#### Requirements
Completed program should:

- Set a maximum number of incorrect guesses and track how many remain.
- Reduce the remaining attempts for each incorrect guess.
- End the game when the word is fully guessed or no attempts remain.
- Display a clear win or loss message and reveal the secret word if the player loses.
