"""
Lesson 1 Assignment: Python Basics
==================================

Synchronized topics:
- Variables, data types, and operators
- Conditionals and basic function design

Important:
- This file is a starter scaffold.
- Complete the TODO sections yourself.
"""


# =============================
# Task 1: Simple Calculator
# =============================
"""
Goal:
- Ask the user for two numbers and one operator (+, -, *, /).
- Return the calculated result.

Pseudo-code:
1. Read two numeric inputs.
2. Read an operator string.
3. Use conditional logic to match the operator.
4. Handle division-by-zero safely.
5. Print the final result.
"""


def calculate(num_one, num_two, operator):
    """
    Calculate a result using two numbers and one operator.

    Args:
        num_one (float): First number.
        num_two (float): Second number.
        operator (str): Arithmetic operator (+, -, *, /).

    Returns:
        float | str: Numeric result or a friendly error message.
    """
    # TODO: Implement operator handling with if/elif/else.
    # TODO: Add division-by-zero protection.
    if operator == "+":
        return num_one + num_two
    elif operator == "-":
        return num_one - num_two
    elif operator == "*":
        return num_one * num_two
    elif operator == "/":
        if num_two != 0:
            return num_one / num_two
        else:
            return "Error: number_two cannot be zero"
    else:
        return "Error: operator must be +, -, *, /"

pass


# =============================
# Task 2: Area of a Rectangle
# =============================
"""
Goal:
- Compute rectangle area using length and width values.

Pseudo-code:
1. Read length and width inputs.
2. Convert inputs to numbers.
3. Validate that both values are positive.
4. Calculate area.
5. Print the area.
"""


def rectangle_area(length, width):
    """
    Return the area of a rectangle.

    Args:
        length (float): Rectangle length.
        width (float): Rectangle width.

    Returns:
        float: Computed area.
    """
    # TODO: Validate inputs and return the computed area.
    if length <= 0 or width <= 0:
        return "Error: length and width must be positive"
    else:
        return length * width
pass


if __name__ == "__main__":
    # TODO: Collect inputs and call `calculate`.
    print("Let's start with the numbers for the calculation.")
    num_one = float(input("Enter a number: "))
    num_two = float(input("Enter a second number: "))
    operator = input("Enter a operator (+, -, *, /): ")
    result = calculate(num_one, num_two, operator)
    print("The result is: ", result)

    # TODO: Collect inputs and call `rectangle_area`.
    print("Let's continue with the rectangle area calculation.")
    length = float(input("Enter a length: "))
    width = float(input("Enter a second width: "))
    result_area = rectangle_area(length, width)
    print("The rectangle area result is: ", result_area)

    pass
