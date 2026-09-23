"""
Helper functions for the Hangman game.
"""


def is_valid_guess(guess):
    """Return True if the guess is exactly one letter."""
    # Check the guess has length 1.
    # Check the guess is a letter, not a number or symbol.
    return len(guess) == 1 and guess.isalpha()


def has_won(secret_word, guessed_letters):
    """Return True if every letter in the word has been guessed."""
    # Turn the word into a set of unique letters.
    # Check if all of them are in guessed_letters.
    return set(secret_word) <= guessed_letters


def format_guessed(guessed_letters):
    """Return guessed letters as sorted, comma-separated text."""
    # Sort the letters alphabetically.
    # Join them with commas.
    return ", ".join(sorted(guessed_letters))


def wants_replay(answer):
    """Return True if the answer means play again."""
    # Clean the answer.
    # Accept "y" or "yes".
    return answer.strip().lower() in ("y", "yes")

def split_guesses(secret_word, guessed_letters):
    """Return (correct, wrong) guesses as sorted text."""
    # Correct: guessed letters that appear in the word.
    # Wrong: guessed letters that do not appear in the word.
    # Format each group with format_guessed.
    correct = {letter for letter in guessed_letters if letter in secret_word}
    wrong = guessed_letters - correct
    return format_guessed(correct), format_guessed(wrong)