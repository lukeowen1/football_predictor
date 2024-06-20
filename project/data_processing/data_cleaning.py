"""
This script takes our dataframe of all the CSVs and cleans it for ML.
We will remove unnecessary fields/columns and ensure there is only one column per field.
"""

import data_processing.data_collation as data_collation
import config as configuration
import pandas as pd

def main(Setup):
    # Load configuration
    config = configuration.load_config()

    columns_to_keep = config["data_cleaning"]["columns_to_keep"]
    excess_columns = config["data_cleaning"]["excess_columns"]
    column_mappings = config["data_cleaning"]["column_mappings"]

    # Import the dataframe created in data_collation.py
    df = data_collation.main(Setup)

    # Filter based on the columns required
    df = df[columns_to_keep + excess_columns]

    # Merge columns as the CSV data structure wasn't consistent

    for main_col, backup_col in column_mappings.items():
        if main_col in df.columns and backup_col in df.columns:
            df[main_col] = df[main_col].combine_first(df[backup_col])

    # Drop the excess columns
    df.drop(columns=excess_columns, inplace=True, errors='ignore')

    # Drop rows where all elements are NaN
    df.dropna(how='all', inplace=True)

    # Calculate average goals
    home_avg_goals = df['FTHG'].mean()
    away_avg_goals = df['FTAG'].mean()

    print(f"Home Average Goals: {home_avg_goals}")
    print(f"Away Average Goals: {away_avg_goals}")

    return home_avg_goals, away_avg_goals, df

if __name__ == "__main__":
    Setup = configuration.Setup()
    home_avg_goals, away_avg_goals, cleaned_df = main(Setup)

