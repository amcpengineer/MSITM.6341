"""
Lesson 7 In-Class Exercises (No Answers)
========================================

This file is scaffold-only and aligned with Lesson 7 examples.
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

data = {
    "StudentID": [101, 102, 103, 104, 105, 106, 107],
    "Hours_Studied": [5, 3, 8, 2, 7, 6, 1],
    "Attendance_Rate": [0.9, 0.6, 0.95, 0.5, 0.8, 0.85, 0.4],
    "Assignments_Completed": [10, 7, 12, 6, 11, 10, 4],
    "Passed": [1, 0, 1, 0, 1, 1, 0],
}

df = pd.DataFrame(data)

FEATURES = ["Hours_Studied", "Attendance_Rate", "Assignments_Completed"]
TARGET = "Passed"


def exploration_exercise():
    """
    Inspect the dataset and basic quality metrics.
    """
    # TODO: Print head(), isnull().sum(), and describe().
    print("\nColumn Names:\n", df.head())
    print("\nNulls summatory:\n", df.isnull().sum())
    print("\nDescriptive Stats:\n", df.describe())
    pass


def visualization_exercise():
    """
    Create pairplot and correlation heatmap.
    """
    # TODO: Build pairplot for numeric features.
    # Pairplot to visualize relationship between features
    sns.pairplot(df.drop('StudentID', axis=1))
    plt.show()
    # TODO: Build annotated heatmap.
    plt.figure()
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
    plt.title("Feature Correlation Heatmap")
    plt.show()
    _ = plt, sns
    pass


def preprocessing_exercise():
    """
    Prepare model features and train/test split.
    """
    # TODO: Select feature columns and target.
    X = df[FEATURES]
    y = df[TARGET]

    # TODO: Apply normalization (optional but recommended).
    # Min-max normalization: every feature goes from 0 to 1.
    X = (X - X.min()) / (X.max() - X.min())
    print("\nNormalized Features:\n", X.round(2))

    # TODO: Split into train/test sets.
    # stratify=y keeps both classes (pass and fail) in train and test.
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )
    print(f"\nTrain rows: {len(X_train)}, Test rows: {len(X_test)}")

    return X_train, X_test, y_train, y_test


def modeling_exercise(X_train, X_test, y_train, y_test):
    """
    Train and evaluate a RandomForest classifier.
    """
    # TODO: Initialize model.
    model = RandomForestClassifier(n_estimators=100, random_state=42)

    # TODO: Fit model with training data.
    model.fit(X_train, y_train)

    # TODO: Predict test labels.
    y_pred = model.predict(X_test)

    # TODO: Print accuracy and classification report.
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nAccuracy: {accuracy:.2f}")
    print("\nClassification Report:\n")
    print(classification_report(y_test, y_pred, zero_division=0))

    return model


def feature_importance_exercise(model):
    """
    Plot model feature importance.
    """
    # TODO: Create feature importance DataFrame.
    importance_df = pd.DataFrame(
        {"Feature": FEATURES, "Importance": model.feature_importances_}
    ).sort_values("Importance", ascending=False)
    print("\nFeature Importance:\n", importance_df)

    # TODO: Plot with seaborn bar chart.
    plt.figure()
    sns.barplot(data=importance_df, x="Importance", y="Feature")
    plt.title("Random Forest Feature Importance")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # TODO: Call exercises in order.
    exploration_exercise()
    visualization_exercise()
    X_train, X_test, y_train, y_test = preprocessing_exercise()
    model = modeling_exercise(X_train, X_test, y_train, y_test)
    feature_importance_exercise(model)
    pass
