#edX username: MMD Aziz Musharraf.
#github username:  Aziz Musharraf.
#CS50 Final Project from problem set 09
#Title: The Hangman Game

import random

def choose_word():
    words = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "strawberry", "pineapple", "blueberry", "apricot", "avocado", "blackberry", "cranberry", "grapefruit", "guava", "lemon", "lime", "lychee", "papaya", "peach", "pear", "plum", "raspberry", "watermelon"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def check_guess(word, guessed_letters, guess):
    guessed_letters.add(guess)
    return guess in word

# Represents the different stages of the hangman
def display_hangman(turns_left):
    stages = [
        """
           --------
           |      |
           |
           |
           |
           |
        """,
        """
           --------
           |      |
           |      O
           |
           |
           |
        """,
        """
           --------
           |      |
           |      O
           |      |
           |
           |
        """,
        """
           --------
           |      |
           |      O
           |     /|
           |
           |
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |
           |
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     /
           |
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / \\
           |
        """
    ]
    return stages[6 - turns_left]

def main():
    print("Welcome to Hangman!")
    print("Try to guess the word by suggesting letters.")
    print("You have 7 attempts. Good luck!\n")

    word = choose_word()
    guessed_letters = set()
    max_attempts = 7
    attempts = 0

    while attempts < max_attempts:
        print(f"Word: {display_word(word, guessed_letters)}")
        print(f"Guessed letters: {' '.join(guessed_letters)}")
        print(display_hangman(attempts))
        try:
            guess = input("Guess a letter: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                raise ValueError("Please enter a single alphabetical letter.")

            if guess in guessed_letters:
                print("You've already guessed that letter. Try again.")
                continue

            if check_guess(word, guessed_letters, guess):
                print("Correct!")
            else:
                print("Incorrect!")
                attempts += 1

            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word '{word}'!")
                break
        except ValueError as e:
            print(e)
    else:
        print(f"Sorry, you've run out of attempts. The word was '{word}'.")

if __name__ == "__main__":
    main()
