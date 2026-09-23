"""
Lesson 4 Group Assignment: Hangman
==================================

Synchronized topics:
- Functions and modular design
- Loops, conditionals, and input validation

Important:
- Work in groups of 2-5.
- This file is a scaffold only.
"""
import secrets
from helper import is_valid_guess, has_won, format_guessed, wants_replay, split_guesses

# =============================
# Assignment Directions
# =============================
"""
Build a Hangman game with module-based structure.

Required components:
1. A main script that controls gameplay.
2. A helper module containing reusable functions.
3. Pseudo-code comments describing each function.
4. A replay option.
"""


# =============================
# Pseudo-code Outline
# =============================
"""
1. Choose a secret word from a list.
2. Initialize guessed letters and remaining tries.
3. Show current hidden word state.
4. Ask user for one letter.
5. Validate guess and update game state.
6. Repeat until win or lose.
7. Ask whether to play again.
"""


def choose_word(word_list):
    """
    Select a secret word.

    Args:
        word_list (list[str]): Candidate words.

    Returns:
        str: Secret word.
    """
    # TODO: Return one word from the list.
    return secrets.choice(word_list)
    pass


def display_word(secret_word, guessed_letters):
    """
    Build display text with underscores for missing letters.

    Args:
        secret_word (str): Target word.
        guessed_letters (set[str]): Guessed characters.

    Returns:
        str: Display form of the word.
    """
    # TODO: Build and return masked word string.
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )
    pass


def process_guess(secret_word, guessed_letters, guess, tries_left):
    """
    Update state based on a user guess.

    Args:
        secret_word (str): Target word.
        guessed_letters (set[str]): Existing guesses.
        guess (str): New guess from user.
        tries_left (int): Remaining attempts.

    Returns:
        tuple[set[str], int]: Updated guessed set and tries left.
    """
    # TODO: Update guessed letters and tries.
    guess = guess.strip().lower()

    if guess in guessed_letters:
        return guessed_letters, tries_left

    updated_letters = guessed_letters | {guess}

    if guess not in secret_word:
        tries_left -= 1

    return updated_letters, tries_left
    pass


def play_hangman(secret_word, max_tries=6):
    """
    Run one full game of hangman.

    Args:
        secret_word (str): Target word.
        max_tries (int): Wrong guesses allowed.

    Returns:
        bool: True if the player wins, False otherwise.
    """
    secret_word = secret_word.lower()
    guessed_letters = set()
    tries_left = max_tries

    print("Welcome to Hangman.")

    while tries_left > 0:
        print(f"\nWord: {display_word(secret_word, guessed_letters)}")
        print(f"Tries left: {tries_left}")
        correct, wrong = split_guesses(secret_word, guessed_letters)
        if correct:
            print(f"In the word: {correct}")
        if wrong:
            print(f"Not in the word: {wrong}")

        guess = input("Guess a letter: ").strip().lower()

        if not is_valid_guess(guess):
            print("Enter one letter.")
            continue
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'.")
            continue

        guessed_letters, tries_left = process_guess(
            secret_word, guessed_letters, guess, tries_left
        )

        if guess in secret_word:
            print("Correct.")
        else:
            print("Wrong.")

        if has_won(secret_word, guessed_letters):
            print(f"\nYou win. The word was: {secret_word}")
            return True

    print(f"\nYou lose. The word was: {secret_word}")
    return False


if __name__ == "__main__":
    words = ["python", "variable", "function", "module", "hangman"]
    wins = 0
    games = 0

    while True:
        secret_word = choose_word(words)
        if play_hangman(secret_word):
            wins += 1
        games += 1

        print(f"Score: {wins} wins out of {games} games")

        again = input("\nPlay again? (y/n): ")
        if not wants_replay(again):
            print("Thanks for playing.")
            break
    pass
