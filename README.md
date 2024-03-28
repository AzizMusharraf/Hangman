# MY PROJECT TITLE IS HANGMAN GAME.


## OVERVIEW:
   Hangman is a classic word guessing game where the player tries to guess a hidden word one letter at a time.
   The player has a limited number of incorrect guesses before the game ends.
   This text-based version of Hangman is implemented in Python.

## DESCRIPTION OF THE PROJECT:

# MODULES & FUNCTIONS USED:
   **Random Module**: Used to generate random numbers for choosing a word from a list of words.

   **Project.py**: This file contains the main game logic and functions.

   **Test_Project.py**: This file contains unit tests for the functions in project.py.

   **Requirements.txt**: This file lists the required packages for running the project.

   **Choose_word() function**: This func selects a randomword from a predefined list of words. It uses the random.choice() func to select a word randomly.

   **Display_word(word, guessed_letters) function**: This function returns a string representing the current state of the *word being guessed. It  displays the letters that have been correctly guessed and underscores for letters that have not been guessed yet.

   **Check_guess(word, guessed_letters, guess) function**: This function checks if a guessed letter is in the word. It updates the set of guessed letters and returns a boolean value indicating whether the guess was correct.

   **Display_hangman(turns_left) function**: This function returns a visual representation of the hangman's gallows based on the number of incorrect  guesses remaining. It uses a list of strings to represent each stage of the hangman.

   **Main() function**: The main function of the game that controls the flow of the game. It initializes the game, handles user inputs, calls other   functions to update the game state, and displays the game status.

# FEATURES OF THE GAME:
   **Random Word Selection**: Each game starts with a randomly selected word from a predefined list.

   **Visual Hangman Display**: A simple ASCII art representation of the hangman's gallows is shown, updating with each incorrect  guess.

   **Error Handling**: Invalid inputs, such as non-alphabetical characters or multiple letters in a single guess, are handled gracefully.

   **Limited Attempts**: The player has 7 incorrect guesses before the game ends.

   **Congratulations Message**: When the player correctly guesses the word, a congratulatory message is displayed.

# DESIGN CHOICES MADE FOR THE GAME:
   **Word List**: The game uses a predefined list of words to ensure a consistent experience for players. The list includes a variety of fruits to keep the game interesting and challenging.

   **Visual Representation**: The game includes a simple ASCII art representation of the hangman's gallows to provide a visual indicator of the player's progress and the consequences of incorrect guesses.

   **Error Handling**: The game includes error handling for invalid inputs, such as non-alphabetical characters or multiple letters in a single guess. This helps ensure a smooth user experience.

   **Limited Attempts**: The game limits the player to 7 incorrect guesses before ending the game. This adds a level of difficulty and strategy to the game, encouraging players to guess carefully.

   **Congratulations Message**: When the player correctly guesses the word, the game displays a congratulatory message with the word they guessed. This provides a sense of accomplishment for the player.

# HOW TO PLAY THE GAME:
  The Hangman game is a word-guessing game where one player thinks of a word and the other player tries to guess it by suggesting letters within a certain number of guesses. Here's how the game typically works:

  **Setting Up**: One player (the "chooser") selects a word in secret. This word is typically a common word or phrase but can be anything they choose. The word should be written down, with blanks for each letter, to represent the word to be guessed.

  **Starting the Game**: The other player (the "guesser") starts the game by guessing a letter of the alphabet.

  **Checking the Guess**: If the guessed letter is in the word, the chooser fills in all instances of that letter in the blanks. If the guessed letter is not in the word, the chooser draws part of a hangman gallows and figure as a tally mark (starting with the gallows, then the head, body, arms, and legs) to indicate the incorrect guess.

  **Guessing the Word**: The guesser continues to guess letters one at a time. Each correct guess fills in more of the word, and each incorrect guess adds another part to the hangman figure. The game continues until either the guesser correctly guesses the word (by filling in all the blanks) or the hangman figure is complete (indicating too many incorrect guesses).

  **Ending the Game**: The game ends when the word is guessed correctly (win) or when the hangman figure is complete (loss). If the guesser wins, they may get a reward or continue with another round. If they lose, the chooser reveals the word, and they may switch roles for the next round.
