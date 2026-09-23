"""
Lesson 3 Assignment: OOP and Modules Refactor
=============================================

Synchronized topics:
- Classes and objects
- Encapsulation
- Modules and imports

Objective:
- Refactor a command-line game (or similar app) using class-based design
  and separate modules.
"""
import secrets

# =============================
# Assignment Prompt
# =============================
"""
Create an object-oriented version of your previous game/app:
1. Build a class that controls game state (scores, rounds, options).
2. Build a helper module for utility functions (validation, formatting, etc.).
3. Keep your main file focused on program flow only.
4. Add simple text logging for each round to a file.
"""


class GameManager:
    """
    Manage game state and round flow.
    """

    def __init__(self):
        """Initialize game configuration and score tracking."""
        # TODO: Add attributes for score, valid choices, and round count.
        self.score = 0
        self.valid_choices = ["Rock", "Paper", "Scissors"]
        self.round_count = 0
        pass

    def play_round(self, user_choice):
        beats = {
            "Rock": "Scissors",
            "Paper": "Rock",
            "Scissors": "Paper",
        }

        user_choice = user_choice.strip().capitalize()
        if user_choice not in self.valid_choices:
            return "Invalid choice"

        self.round_count += 1
        computer_choice = secrets.choice(self.valid_choices)

        if user_choice == computer_choice:
            return f"Tie. Both chose {computer_choice}"
        if beats[user_choice] == computer_choice:
            self.score += 1
            return f"User wins. {user_choice} beats {computer_choice}"
        return f"Computer wins. {computer_choice} beats {user_choice}"
        pass

    def summary(self):
        """
        Return final game summary text.

        Returns:
            str: Summary for player and computer score.
        """
        # TODO: Build and return summary message.
        return f"Player score = {self.score}/ Over this rounds = {self.round_count}"
        pass


class Logger:
    """
    Simple text logger for assignment events.
    """

    def __init__(self, filename):
        """
        Store output log filename.

        Args:
            filename (str): Log file path.
        """
        self.filename = filename

    def write_line(self, message):
        """
        Append one message line to the log file.

        Args:
            message (str): Text line to write.
        """
        # TODO: Append message to file using `with open(..., "a")`.
        with open(self.filename, "a", encoding="utf-8") as file:
            file.write(message + "\n")
        pass


def main():
    """
    Entry point for your class-based assignment.
    """
    # TODO: Initialize GameManager and Logger.
    # TODO: Build input loop and call play_round().
    # TODO: Print final summary.
    game = GameManager()
    logger = Logger("game_log.txt")
    logger.write_line("Game started")

    print("Rock, Paper, Scissors")
    print("Type Rock, Paper, or Scissors. Type Q to quit.")

    while True:
        user_choice = input("\nYour choice: ").strip()

        if user_choice.lower() == "q":
            break

        result = game.play_round(user_choice)
        print(result)

        if result != "Invalid choice":
            logger.write_line(f"Round {game.round_count}: {result}")

    summary = game.summary()
    print("\nGame over.")
    print(summary)
    logger.write_line(summary)
    logger.write_line("Game ended")
    pass


if __name__ == "__main__":
    main()
