"""
Lesson 6 Take-Home Assignment: Kaggle Dataset EDA
=================================================

Synchronized topics:
- Data loading and inspection
- Missing-value handling
- Descriptive statistics
- Visualization with matplotlib/seaborn

Important:
- This is a scaffold only; implement all TODO sections.
"""
import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def load_dataset(file_name):
    """
    Load a CSV file selected by the student.

    Args:
        file_name (str): CSV filename.

    Returns:
        pandas.DataFrame: Loaded dataset.
    """
    # TODO: Implement safe CSV loading with error handling.
    if not file_name.lower().endswith(".csv"):
        print(f"Error: '{file_name}' is not a CSV file. Use a file that ends with .csv.")
        return None

    if not os.path.exists(file_name):
        print(f"Error: '{file_name}' does not exist. Check the name and folder.")
        return None

    try:
        df = pd.read_csv(file_name)
    except pd.errors.EmptyDataError:
        print(f"Error: '{file_name}' is empty.")
        return None
    except pd.errors.ParserError:
        print(f"Error: '{file_name}' is not a valid CSV file.")
        return None
    except UnicodeDecodeError:
        df = pd.read_csv(file_name, encoding="latin-1")

    print(f"Loaded '{file_name}': {df.shape[0]} rows, {df.shape[1]} columns.")
    return df


def clean_dataset(df):
    """
    Apply missing-value strategy chosen by the user.

    Args:
        df (pandas.DataFrame): Raw dataset.

    Returns:
        pandas.DataFrame: Cleaned dataset.
    """
    # Check for missing values first.
    missing = df.isnull().sum()
    missing = missing[missing > 0]
    if missing.empty:
        print("No missing values found. Nothing to clean.")
        return df

    print("Missing values per column:")
    for column, count in missing.items():
        print(f"  {column} ({df[column].dtype}): {count} missing")

    # TODO: Prompt user to choose fill vs drop strategy.
    while True:
        strategy = input("Enter fill or drop for the clean strategy: ").strip().lower()
        if strategy in ("fill", "drop"):
            break
        print("Invalid choice. Type fill or drop.")

    # TODO: Apply the selected cleaning method.
    df_clean = df.copy()

    if strategy == "drop":
        df_clean = df_clean.dropna()
        print(f"Dropped {len(df) - len(df_clean)} rows with missing values.")
    else:
        for column in missing.index:
            if pd.api.types.is_numeric_dtype(df_clean[column]):
                fill_value = df_clean[column].mean()
                print(f"  {column}: numeric, filled with mean {fill_value:.2f}")
            else:
                fill_value = df_clean[column].mode()[0]
                print(f"  {column}: text, filled with mode '{fill_value}'")
            df_clean[column] = df_clean[column].fillna(fill_value)

    return df_clean


def summarize_column(df, column_name):
    """
    Print descriptive statistics for one selected column.

    Args:
        df (pandas.DataFrame): Dataset.
        column_name (str): Column to summarize.
    """
    # TODO: Validate column and print useful summary stats.
    if column_name not in df.columns:
        print(f"Error: '{column_name}' is not a column.")
        print(f"Available columns: {list(df.columns)}")
        return

    column = df[column_name]
    print(f"\nSummary for '{column_name}' ({column.dtype}):")
    print(column.describe())
    print(f"Missing values: {column.isnull().sum()}")


def choose_option(options, label):
    """Show a numbered menu and return the option the user picks."""
    print(f"\nSelect {label}:")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    while True:
        choice = input(f"Enter the {label} number: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]
        print(f"Invalid choice. Enter a number from 1 to {len(options)}.")


def create_visualizations(df):
    """
    Generate at least two visualizations.

    Args:
        df (pandas.DataFrame): Dataset to plot.
    """
    # TODO: Ask user for plot choices and generate charts.
    # Suggested options: histogram, boxplot, scatterplot, countplot.
    numeric_cols = list(df.select_dtypes(include="number").columns)
    text_cols = list(df.select_dtypes(exclude="number").columns)

    plots = ["Histogram", "Boxplot", "Scatterplot", "Countplot", "Finish"]
    charts_made = 0

    while True:
        selected_plot = choose_option(plots, "plot")

        if selected_plot == "Finish":
            if charts_made >= 2:
                break
            print(f"You need at least 2 charts. You have {charts_made}.")
            continue

        plt.figure()

        match selected_plot:
            case "Histogram":
                if not numeric_cols:
                    print("No numeric columns available for a histogram.")
                    plt.close()
                    continue
                column = choose_option(numeric_cols, "column")
                sns.histplot(data=df, x=column, kde=True)
                plt.title(f"Distribution of {column}")

            case "Boxplot":
                if not numeric_cols:
                    print("No numeric columns available for a boxplot.")
                    plt.close()
                    continue
                column = choose_option(numeric_cols, "column")
                sns.boxplot(data=df, y=column)
                plt.title(f"Boxplot of {column}")

            case "Scatterplot":
                if len(numeric_cols) < 2:
                    print("A scatterplot needs at least 2 numeric columns.")
                    plt.close()
                    continue
                x_col = choose_option(numeric_cols, "X axis column")
                y_options = [col for col in numeric_cols if col != x_col]
                y_col = choose_option(y_options, "Y axis column")
                sns.scatterplot(data=df, x=x_col, y=y_col)
                plt.title(f"{x_col} vs {y_col}")

            case "Countplot":
                if not text_cols:
                    print("No text columns available for a countplot.")
                    plt.close()
                    continue
                column = choose_option(text_cols, "column")
                sns.countplot(data=df, x=column)
                plt.title(f"Count of {column}")

        plt.tight_layout()
        plt.show()
        charts_made += 1
        print(f"Charts created: {charts_made}")


def main():
    """
    Orchestrate Lesson 6 assignment steps.
    """
    file_name = input(
        "Enter your Kaggle dataset CSV filename (including .csv): "
    ).strip()

    # TODO: Call load_dataset().
    df = load_dataset(file_name)
    if df is None:
        print("Stopping: the dataset could not be loaded.")
        return

    # TODO: Show dataset overview (head/info/missing values).
    print("\n--- Dataset Overview ---")
    print("\nFirst Rows:\n", df.head())
    print("\nColumn Info:")
    df.info()
    print("\nMissing Values per Column:\n", df.isnull().sum())

    # TODO: Call clean_dataset().
    print("\n--- Cleaning ---")
    df = clean_dataset(df)
    print(f"Remaining missing values: {df.isnull().sum().sum()}")

    # TODO: Call summarize_column().
    print("\n--- Column Summary ---")
    column_name = choose_option(list(df.columns), "column to summarize")
    summarize_column(df, column_name)

    # TODO: Call create_visualizations().
    print("\n--- Visualizations ---")
    create_visualizations(df)

    print("\nEDA complete.")


if __name__ == "__main__":
    main()
