"""Train a multiple regression model from train_data.csv and save weights.

The CSV is expected to have no header and exactly three numeric columns:
column 0 -> feature 1
column 1 -> feature 2
column 2 -> target

The saved JSON file can be loaded by another Python script to make predictions
using: intercept + coefficient_1 * x1 + coefficient_2 * x2
"""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression


def train_model(input_csv: str = "train_data.csv", output_file: str = "trained_weights.json") -> dict:
    data_path = Path(input_csv)
    if not data_path.exists():
        raise FileNotFoundError(f"Training data file not found: {data_path}")

    data = pd.read_csv(data_path, header=None)
    if data.shape[1] < 3:
        raise ValueError("Expected at least 3 columns: x1, x2, y")

    features = data.iloc[:, :2]
    target = data.iloc[:, 2]

    model = LinearRegression()
    model.fit(features, target)

    weights = {
        "input_columns": [0, 1],
        "target_column": 2,
        "intercept": float(model.intercept_),
        "coefficients": [float(value) for value in model.coef_],
        "feature_names": ["x1", "x2"],
    }

    output_path = Path(output_file)
    output_path.write_text(json.dumps(weights, indent=2), encoding="utf-8")
    return weights


def main() -> None:
    weights = train_model()
    print("Model trained successfully.")
    print(f"Intercept: {weights['intercept']}")
    print(f"Coefficients: {weights['coefficients']}")
    print("Saved weights to trained_weights.json")


if __name__ == "__main__":
    main()