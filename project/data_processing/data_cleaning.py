"""
This script takes our dataframe of all the CSVs and cleans it for ML.
We will remove unneccesary fields / columns and ensure there is only 1 column per field. 
"""

import data_processing.data_collation as data_collation
import config as configuration 

def main(Setup): 

    config = configuration.load_config()

    columns_to_keep = config["data_cleaning"]["columns_to_keep"]
    excess_columns = config["data_cleaning"]["excess_columns"]

    # import the dataframe created in data_collation.py 
    df = data_collation.main(Setup)
    
    # filter based on the columns required
    df = df[columns_to_keep + excess_columns]

    # Merge columns as the CSV data structure wasn't consistent
    
    df['FTHG'].fillna(df['Full time home goals'], inplace=True)
    df['FTAG'].fillna(df['Full time away goals'], inplace=True)
    df['FTR'].fillna(df['Full time result'], inplace=True)
    df['HS'].fillna(df['Home shots'], inplace=True)


    # Drop the excess columns

    for column in excess_columns:
        df.drop([column], axis=1, inplace=True)

    print(df)

    
    
    

 







