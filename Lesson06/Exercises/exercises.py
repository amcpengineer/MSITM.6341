"""
Lesson 6 In-Class Exercises (No Answers)
========================================

This file is scaffold-only and aligned with Lesson 6 examples.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

data = {
    "Player": [
        "LeBron James",
        "Stephen Curry",
        "Kevin Durant",
        "Giannis Antetokounmpo",
        "Nikola Jokic",
        "Luka Doncic",
        "Joel Embiid",
        "James Harden",
        "Jayson Tatum",
        "Devin Booker",
    ],
    "Team": [
        "Lakers",
        "Warriors",
        "Nets",
        "Bucks",
        "Nuggets",
        "Mavericks",
        "76ers",
        "76ers",
        "Celtics",
        "Suns",
    ],
    "Position": ["SF", "PG", "SF", "PF", "C", "PG", "C", "SG", "SF", "SG"],
    "PPG": [27.3, 29.6, 28.5, 29.9, 26.2, 30.2, 33.1, 21.3, 26.7, 27.0],
    "APG": [7.4, 6.3, 5.2, 5.9, 7.8, 8.1, 4.3, 10.5, 4.4, 4.8],
    "RPG": [7.9, 4.5, 7.4, 11.7, 13.8, 9.1, 10.6, 6.2, 8.5, 5.1],
}

df_nba = pd.DataFrame(data)


def numpy_exercise():
    """
    Practice NumPy matrix creation and summary statistics.
    """
    # TODO: Ask for matrix size.
    size = int(input("Enter matrix size: "))

    # TODO: Create random square matrix.
    matrix = np.random.randint(1,10,size=(size,size))
    print("\n2D Matrix:\n", matrix)
    # TODO: Compute row and column means.
    _ = np
    pass


def pandas_filter_exercise():
    """
    Practice DataFrame filtering based on user input.
    """
    # TODO: Ask for team filter and print matching rows.
    teams = sorted(df_nba["Team"].unique())

    print("Select a Team:")
    for i, team in enumerate(teams,start=1):
        print(f"{i}. {team}")

    while True:
        team_chose = input("Enter the team number:")
        if team_chose.isdigit() and 1 <= int(team_chose) <= len(teams) :
            selected_team = teams[int(team_chose)-1]
            break
        print(f"Invalid choise. Enter a number from 1 to {len(teams)}")

    print("You selected: ", selected_team)

    filtered_df = df_nba[df_nba["Team"] == selected_team]
    print("Data filtered is", filtered_df)

    _ = df_nba
    pass


def normalization_exercise():
    """
    Practice min-max normalization on one selected stat column.
    """
    # TODO: Ask for one column (PPG/APG/RPG).
    columns = ["PPG", "APG", "RPG"]
    print("Select one column number:")
    for i, column in enumerate(columns, start=1):
        print(f"{i}. {column}")

    # TODO: Validate selection.
    while True:
        choice = input("Enter the column number: ")
        if choice.isdigit() and 1 <= int(choice) <= len(columns):
            selected_column = columns[int(choice) - 1]
            break
        print(f"Invalid choice. Enter a number from 1 to {len(columns)}.")
    print("You selected to normalize: ", selected_column)

    # TODO: Create normalized column.
    col = df_nba[selected_column]
    normalized_name = f"{selected_column}_normalized"
    df_nba[normalized_name] = (col - col.min()) / (col.max() - col.min())

    print(df_nba[["Player", selected_column, normalized_name]])
    pass


def eda_exercise():
    """
    Compute aggregate stats for one selected numeric column.
    """
    # TODO: Ask for target column and print mean/median/std.
    columns = ["PPG", "APG", "RPG"]
    print("Select one column number:")
    for i, column in enumerate(columns, start=1):
        print(f"{i}. {column}")
    pass

    while True:
        choice = input("Enter the column number: ")
        if choice.isdigit() and 1 <= int(choice) <= len(columns):
            selected_column = columns[int(choice) - 1]
            break
        print(f"Invalid choice. Enter a number from 1 to {len(columns)}.")
    print("You selected to normalize: ", selected_column)

    print("\nMean of the Column:", df_nba[selected_column].mean())
    print("\nMedian of the Column:", df_nba[selected_column].median())
    print("\nDescriptive Statistics of the Column:\n",df_nba[selected_column].describe())

def visualization_exercise():
    """
    Generate one selected chart.
    """
    # TODO: Ask which plot to generate.
    plots = ["Histogram", "Scatter", "Boxplot"]
    print("Select one option to plot:")
    for i, plot in enumerate(plots, start=1):
        print(f"{i}. {plot}")

    # TODO: Validate selection.
    while True:
        choice = input("Enter the plot number: ")
        if choice.isdigit() and 1 <= int(choice) <= len(plots):
            selected_plot = plots[int(choice) - 1]
            break
        print(f"Invalid choice. Enter a number from 1 to {len(plots)}.")
    print("You selected to plot a", selected_plot)

    # TODO: Build histogram OR scatter OR boxplot.
    # Setting style for seaborn
    sns.set_style("whitegrid")

    match selected_plot:
        case "Histogram":
            plt.hist(df_nba["PPG"], bins=5, edgecolor="black")
            plt.title("Points per game distribution")
            plt.xlabel("PPG")
            plt.ylabel("Number of players")

        case "Scatter":
            plt.scatter(df_nba["PPG"], df_nba["APG"])
            plt.title("Points vs assists per game")
            plt.xlabel("PPG")
            plt.ylabel("APG")

        case "Boxplot":
            plt.boxplot([df_nba["PPG"], df_nba["APG"], df_nba["RPG"]],
                        tick_labels=["PPG", "APG", "RPG"])
            plt.title("Stat distributions")
            plt.ylabel("Value")

    plt.tight_layout()
    plt.show()

    _ = plt, sns
    pass


if __name__ == "__main__":
    # TODO: Call each exercise function in sequence.
    numpy_exercise()
    pandas_filter_exercise()
    normalization_exercise()
    eda_exercise()
    visualization_exercise()
    pass
