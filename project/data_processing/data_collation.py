"""
This is the main 'data collation' script that gets imported when main.py is run. 
This script takes all the downloaded CSVs and combines them into 1 dataframe.
"""

import pandas as pd
import glob
import config as configuration 


def main(Setup):

    config = configuration.load_config()

    csv_file_path = config["data_collation"]["csv_file_path"]

    # Get a list of all CSV files in the directory
    csv_list = glob.glob(csv_file_path)

    # Create an empty dataframe to store the combined data
    df_football = pd.DataFrame()

    # Iterate over each CSV file and append its data to the combined dataframe
    for file in csv_list:
        df = pd.read_csv(file)
        df_football = df_football._append(df, ignore_index=True)

    df_football.to_csv('df.csv')

    return(df_football)

    


