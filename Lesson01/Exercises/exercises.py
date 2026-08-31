"""
Lesson 1 In-Class Exercises (No Answers)
========================================

This file is intentionally scaffold-only.
Implement each TODO during class.
"""

# ========================
# Section 1: Variables
# ========================

# Exercise 1:
# TODO: Define variables for student name and age.
student_name = ""
student_age = 0
# TODO: Print a sentence using f-string formatting.
print(f"Student name is: {student_name}, and student age is: {student_age}")

# Exercise 2:
# TODO: Convert two string numbers to integers.
my_age = "34"
average_age = "20"

my_age_int = int(my_age)
average_age_int = int(average_age)

# TODO: Print their sum and division result.
print(f"Sum of numbers = {my_age_int + average_age_int}, and division = {my_age_int / average_age_int}")

# ========================
# Section 2: Data Types
# ========================

# Exercise 3:
# TODO: Create int, float, str, and bool variables.
age = 33 #int
height = 1.8 #float
name = "Angela" #str
is_graduated = False #bool
# TODO: Print each variable's data type.
print(type(age))
print(type(height))
print(type(name))
print(type(is_graduated))

# ========================
# Section 3: Operators
# ========================

# Exercise 4:
# TODO: Define two numbers.
number_one = 33
number_two = 5
# TODO: Print +, -, *, /, and % results.
print(f"Sum = {number_one + number_two}")
print(f"Subs = {number_one - number_two}")
print(f"Mult = {number_one * number_two}")
print(f"Div = {number_one / number_two}")
print(f"Modulus = {number_one % number_two}")

# ========================
# Section 4: Control Flow
# ========================

# Exercise 5:
# TODO: Write an if/elif/else block to classify a number as positive, negative, or zero.
number_to_classify = 0
clasification_result = ""
if (number_to_classify > 0):
    clasification_result = "Positive"
elif (number_to_classify < 0):
    clasification_result = "Negative"
elif (number_to_classify == 0):
    clasification_result = "Zero"

print(f"Clasification result: {clasification_result}")

# Exercise 6:
# TODO: Determine whether a number is even or odd.
exercise_input_number = 10
modulus = exercise_input_number % 2
print(f"Modulus: {modulus}")
if (modulus > 0):
    print(f"The number is = odd")
else:
    print(f"The number is = even")



# Exercise 7:
# TODO: Use a for-loop to print values 1 through 5.
for index in range(1, 6):
    print(f"Iteration {index}")

# Exercise 8:
# TODO: Compute factorial using a while-loop.
number_to_compute_factorial = 5
factorial = 1
while(number_to_compute_factorial > 1):
    factorial = factorial * number_to_compute_factorial
    number_to_compute_factorial = number_to_compute_factorial - 1
print(factorial)


# ========================
# Section 5: Functions
# ========================


def add_numbers(left, right):
    """
    Return the sum of two values.

    Args:
        left (int | float): First value.
        right (int | float): Second value.

    Returns:
        int | float: Sum result.
    """
    # TODO: Implement addition logic.
    return left + right
    pass


def greet_user(name="Guest"):
    """
    Return a greeting message.

    Args:
        name (str): Optional name to greet.

    Returns:
        str: Greeting text.
    """
    # TODO: Return greeting string.
    print(f"Hello, {name}!")
    pass


if __name__ == "__main__":
    # TODO: Call `add_numbers` with sample values.
    print(add_numbers(10, 20))
    # TODO: Call `greet_user` with and without an argument.
    greet_user("Angela")
    pass
