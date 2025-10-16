
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman word-guessing game using Python to practice string manipulation, loops, conditionals, and user input handling. You'll create an interactive game where players guess letters to reveal a hidden word before running out of attempts.

## 📝 Tasks

### 🛠️ Word Selection and Display

#### Description
Create the foundation of your game by implementing random word selection and displaying the current state of the word to the player.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list of at least 5 different words
- Display the word as underscores with spaces (e.g., `_ _ _ _` for a 4-letter word)
- Update the display to reveal correctly guessed letters in their proper positions
- Keep unguessed letters hidden as underscores throughout the game


### 🛠️ Game Logic and Input Validation

#### Description
Implement the core game mechanics including accepting player guesses, validating input, and tracking game progress.

#### Requirements
Completed program should:

- Accept single letter guesses from the player (case-insensitive)
- Validate that input is a single letter (reject numbers, special characters, and multiple letters)
- Track the number of incorrect guesses remaining (start with 6 attempts)
- Prevent duplicate guesses and notify the player if a letter was already tried
- Display a list of previously guessed letters to help the player


### 🛠️ Win/Lose Conditions

#### Description
Determine when the game ends and provide appropriate feedback to the player.

#### Requirements
Completed program should:

- End the game when the word is completely guessed (player wins)
- End the game when all attempts are used (player loses)
- Display a congratulatory message when the player wins
- Display an encouraging message with the correct word revealed when the player loses
- Ask if the player wants to play again after each game
