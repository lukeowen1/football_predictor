import pandas as pd
import glob
import config as configuration 

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.options.mode.chained_assignment = None

def main(Setup):

    config = configuration.load_config()

    csv_files = config["data_collation"]["csv_file_path"]


# Get a list of all CSV files in the directory
csv_files = glob.glob('/Users/lwowen/Library/CloudStorage/OneDrive-Deloitte(O365D)/Documents/prem_league_data/*.csv')

# Create an empty dataframe to store the combined data
df_football = pd.DataFrame()

# Iterate over each CSV file and append its data to the combined dataframe
for file in csv_files:
    df = pd.read_csv(file)
    df_football = df_football._append(df, ignore_index=True)

print(df_football)


