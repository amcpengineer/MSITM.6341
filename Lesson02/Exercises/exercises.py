"""
Lesson 2 In-Class Exercises (No Answers)
========================================

This file is scaffold-only.
Use the matching examples file as your reference.
"""

import random


# =============================
# Exercise 1: Collections Practice
# =============================

# TODO: Create an `inventory` dictionary with nested details.
# TODO: Add one new product.
# TODO: Update stock for one product.
# TODO: Loop through inventory and print a summary.

inventory = {
    "Apple": {"quantity":"1"},
    "Orange": {"quantity":"4"},
}

inventory["Banana"] = {"quantity":"2"}
inventory["Apple"] = {"quantity":"3"}

for product_name, details in inventory.items():
    print(f"{product_name}: {details['quantity']} in stock")

# =============================
# Exercise 2: Student Tracker
# =============================

# TODO: Create a nested dictionary for students and grades.
# TODO: Add one student.
# TODO: Update one existing grade.
# TODO: Compute and print each student's average.
students_dictionary = {
    "Angela": {"Subjects":["Math","Physics","Chemistry"],"Grades":[10,7,6] },
    "Camilo": {"Subjects": ["Math", "Physics", "Chemistry"], "Grades": [6, 7, 10]},
}

students_dictionary["Patricia"] = {"Subjects": ["Python", "Physics", "Chemistry"], "Grades": [6,7, 10]}

students_dictionary["Camilo"]["Grades"][1] = 10

for student_name, details in students_dictionary.items():
    average_grade = sum(details["Grades"]) / len(details["Grades"])
    print(f"{student_name}: {average_grade}")

# =============================
# Exercise 3: Indexing and Slicing
# =============================

# TODO: Create a sentence string.
# TODO: Print first N characters, last N characters, and a stepped slice.

sentence = "Hi world"
first_letter = sentence[0]
last_letter = sentence[-1]
slice = sentence[::2]
print(first_letter, last_letter, slice)

# =============================
# Exercise 4: Control Flow
# =============================

# TODO: Iterate through a list of integers.
# TODO: Print whether each number is positive, negative, or zero.
integers_list = [-50, 1, 0]
for integer in integers_list:
    if integer < 0:
        print(f"{integer} is negative")
    if integer > 0:
        print(f"{integer} is positive")
    if integer == 0:
        print(f"{integer} is zero")


# =============================
# Exercise 5: Function + Scope
# =============================

course_name = "MSITM.6341"


def summarize_student(name, grades):
    """
    Build a student summary with average grade.

    Args:
        name (str): Student name.
        grades (list[int | float]): Numeric grades.

    Returns:
        str: Summary line.
    """
    # TODO: Compute average and return formatted summary.
    average_grade = sum(grades) / len(grades)
    return print(f"{name} - average grade: {average_grade}")
    pass


# =============================
# Exercise 6: Pseudo-code to Python
# =============================

"""
Pseudo-code for Rock, Paper, Scissors
1. Store valid choices.
2. Read player choice.
3. Randomly choose computer choice.
4. Compare choices to determine winner.
"""


def determine_rps_winner(player_choice, computer_choice):
    """
    Return round outcome for Rock-Paper-Scissors.

    Args:
        player_choice (str): User choice.
        computer_choice (str): Computer choice.

    Returns:
        str: "Player wins", "Computer wins", or "Tie".
    """
    # TODO: Implement winner logic.
    valid_choices = ["Rock", "Paper", "Scissors"]
    if player_choice not in valid_choices:
        return f"{player_choice} is not a valid choice."
    if computer_choice not in valid_choices:
        return f"{computer_choice} is not a valid choice."
    if player_choice == computer_choice:
        return "Tie"

    beats = {
        "Rock": "Scissors",
        "Paper": "Rock",
        "Scissors": "Paper",
    }

    if beats[player_choice] == computer_choice:
        return "Player wins"
    return "Computer wins"

    pass


if __name__ == "__main__":
    # TODO: Add quick test run with one random computer choice.
    valid_choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(valid_choices)
    print("Computer choice:", computer_choice)
    player_choice = "Rock"  # hardcoded for a quick test

    result = determine_rps_winner(player_choice, computer_choice)
    print(result)

    pass
