#!/usr/bin/env python3
"""
Lesson 5 In-Class Exercises (No Answers)
========================================

This file is scaffold-only.
Complete each TODO step during class.
"""

import csv
import json
import os

import requests

try:
    import pandas as pd
except ImportError:
    pd = None

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def exercise_1():
    """
    API Data Fetch and CSV Conversion.
    """
    print("\n--- Exercise 1 ---")
    url = "https://jsonplaceholder.typicode.com/posts"

    # TODO: Request data from API and handle errors.
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print(f"Fetched {len(data)} posts.")
    except requests.exceptions.RequestException as e:
        print("Error fetching data from API:", e)
        return

    # TODO: Save data to `posts.json`.
    with open("posts.json","w",encoding="utf-8") as f:
        json.dump(data,f,indent=2)
    print("Saved data to posts.json")


    # TODO: Read `posts.json`.
    with open("posts.json", "r", encoding="utf-8") as f:
        posts = json.load(f)
    print(f"Read {len(posts)} posts from posts.json")

    # TODO: Export selected fields to `posts.csv`.
    fields = ["userId", "id", "title"]
    with open("posts.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(posts)
    print(f"Exported fields {fields} to posts.csv")
    pass


def exercise_2():
    """
    Directory analysis and file manipulation.
    """
    print("\n--- Exercise 2 ---")
    dir_name = "data"
    current_dir = os.getcwd()
    print(f"Current working directory: {current_dir}")

    # TODO: Create `data` directory if missing.
    new_dir = os.path.join(current_dir, dir_name)
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)
        print(f"Created directory: {new_dir}")
    else:
        print(f"Directory already exists: {new_dir}")

    # TODO: Create `file1.txt`, `file2.txt`, `file3.txt`.
    filename_one = "file1.txt"
    filename_two = "file2.txt"
    filename_three = "file3.txt"
    with open(filename_one, 'w'):
        pass

    with open(filename_two, 'w'):
        pass

    with open(filename_three, 'w'):
        pass


    # TODO: Print each file name and file size.
    for filename in [filename_one, filename_two, filename_three]:
        size = os.path.getsize(filename)
        print(f"{filename}: {size} bytes")
    _ = dir_name
    pass


def exercise_3():
    """
    CSV -> JSON pipeline with optional pandas analysis.
    """
    print("\n--- Exercise 3 ---")
    csv_filename = "students.csv"
    json_filename = "students.json"

    # TODO: Create CSV with header and sample rows.
    header = ["Name", "Age", "Grade"]
    rows = [
        ["Alice", 18, "A"],
        ["Bob", 19, "B"],
        ["Charlie", 18, "C"]
    ]

    with open(csv_filename, "w", newline="", encoding="utf-8") as f:
        write = csv.writer(f)
        write.writerow(header)
        write.writerows(rows)
    print(f"Wrote to {csv_filename}")

    # TODO: Read CSV using DictReader into a list.
    data_list = []
    with open(csv_filename, "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data_list.append(row)
    print(f"Read {len(data_list)} rows from {csv_filename}")

    # TODO: Write list to JSON.
    with open(json_filename, "w", encoding="utf-8") as jsonfile:
        json.dump(data_list,jsonfile,indent=2)
    print(f"Wrote to {json_filename}")

    # TODO: If pandas available, compute average age and grade.
    if pd is None:
        print("Pandas is not installed.")
        return
    df = pd.DataFrame(data_list)
    print("Initial DataFrame:")
    print(df)

    df["Age"] = pd.to_numeric(df["Age"])
    average_age = df["Age"].mean()
    print(f"Average age: {average_age:.2f}" )

    grade_points = {"A":4,"B":3,"C":2,"D":1,"E":0}
    df["GradePoints"] = df["Grade"].map(grade_points)
    average_grade = df["GradePoints"].mean()
    print(f"Average grade points: {average_grade:.2f}")

    grade_points_to_letters = {v : k for k, v in grade_points.items()}
    average_grade_letter = grade_points_to_letters[round(average_grade)]
    print(f"Average grade letter: {average_grade_letter}")


    _ = csv, json, pd, csv_filename, json_filename
    pass


def main_exercises():
    """
    Run all Lesson 5 exercises.
    """
    exercise_1()
    exercise_2()
    exercise_3()


if __name__ == "__main__":
    main_exercises()
