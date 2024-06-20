"""
This is the main 'data collation' script that gets imported when main.py is run.
This script takes all the downloaded CSVs and combines them into 1 dataframe.
"""

import pandas as pd
import glob
import config as configuration
import logging

def main(Setup):
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    
    # Load configuration
    config = configuration.load_config()

    csv_file_path = config["data_collation"]["csv_file_path"]

    # Get a list of all CSV files in the directory
    csv_list = glob.glob(csv_file_path)

    # Create an empty list to store individual DataFrames
    data_frames = []

    # Iterate over each CSV file and append its data to the list of DataFrames
    for file in csv_list:
        try:
            df = pd.read_csv(file)
            data_frames.append(df)
            logging.info(f"Successfully read {file}")
        except Exception as e:
            logging.error(f"Error reading {file}: {e}")

    # Concatenate all DataFrames into one
    df_football = pd.concat(data_frames, ignore_index=True)

    return df_football

if __name__ == "__main__":
    Setup = configuration.Setup()
    combined_df = main(Setup)

