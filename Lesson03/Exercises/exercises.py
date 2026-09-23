"""
Lesson 3 In-Class Exercises (No Answers)
========================================

This file is scaffold-only.
Implement each class/function during practice.
"""
import math
import os

import math_operations
from geometry import circle, rectangle

os.chdir(os.path.dirname(os.path.abspath(__file__)))


# ========================
# Exercise 1: Classes and Objects
# ========================


class Book:
    """Represent one book with core metadata."""

    def __init__(self, title, author, year):
        # TODO: Store constructor inputs as instance attributes.
        self.title = title
        self.author = author
        self.year = year
        pass

    def book_info(self):
        """
        Return one formatted summary string for the book.
        """
        # TODO: Return formatted book description.
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}")
        pass


# ========================
# Exercise 2: Inheritance
# ========================


class Person:
    """Base class for person data."""

    def __init__(self, name, age):
        # TODO: Initialize name and age.
        self.name = name
        self.age = age
        pass

    def get_info(self):
        """Return base info text."""
        # TODO: Return person info string.
        return f"Name: {self.name}, Age: {self.age}"
        pass


class Student(Person):
    """Subclass that adds student-specific data."""

    def __init__(self, name, age, student_id):
        # TODO: Call parent initializer and store student_id.
        super().__init__(name, age)
        self.student_id = student_id
        pass

    def get_info(self):
        """Return combined info including student ID."""
        # TODO: Override and extend parent info.
        return f"{super().get_info()}, Student ID: {self.student_id}"

        pass


# ========================
# Exercise 3: Encapsulation
# ========================


class BankAccount:
    """Practice private attributes and controlled updates."""

    def __init__(self, owner, balance):
        # TODO: Store owner and create private balance.
        self.owner = owner
        self.__balance = balance
        pass

    def deposit(self, amount):
        # TODO:Add validation and update balance.
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount
        pass

    def withdraw(self, amount):
        # TODO: Add validation and update balance.
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance -= amount
        pass


    def get_balance(self):
        # TODO: Return current balance.
        return self.__balance


# ========================
# Exercise 4: Working with Modules
# ========================

# TODO: Call add, subtract, multiply, and divide functions
_ = math_operations
_.add(1,1)
_.subtract(1,1)
_.multiply(1,1)
_.divide(1,1)

# ========================
# Exercise 5: Using Packages
# ========================

# TODO: Call area/circumference helpers from `geometry/circle.py`.
# TODO: Call area helper from `geometry/rectangle.py`.
_ = circle, rectangle
circle.area(2)
circle.circumference(3)
rectangle.area(2,3)
# ========================
# Exercise 6: Polymorphism
# ========================


class Shape:
    """Base class for polymorphism exercise."""

    def area(self):
        # TODO: Return default area value.
        return 0
        pass


class CircleShape(Shape):
    """Circle subclass."""

    def __init__(self, radius):
        # TODO: Store radius.
        self.radius = radius
        pass

    def area(self):
        # TODO: Return circle area.
        return math.pi * (self.radius ** 2)
        pass


class RectangleShape(Shape):
    """Rectangle subclass."""

    def __init__(self, width, height):
        # TODO: Store width and height.
        self.width = width
        self.height = height
        pass

    def area(self):
        # TODO: Return rectangle area.
        return self.width * self.height
        pass


if __name__ == "__main__":
    # TODO: Instantiate each class and print practice results.
    # Exercise 1: Classes and Objects
    book = Book("1984", "George Orwell", 1949)
    print(book.book_info())

    # Exercise 2: Inheritance
    person = Person("Maria", 40)
    student = Student("Angela", 30, "S123")
    print(person.get_info())
    print(student.get_info())

    # Exercise 3: Encapsulation
    account = BankAccount("Angela", 100)
    account.deposit(50)
    account.withdraw(30)
    print("Balance:", account.get_balance())

    # Exercise 6: Polymorphism
    shapes = [Shape(), CircleShape(3), RectangleShape(4, 5)]
    for shape in shapes:
        print(type(shape).__name__, "area:", shape.area())
    pass
