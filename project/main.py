"""
The 'main' script that all other scripts run from. 
This is designed to be ran from the terminal by inputting 'python3 main.py'
""" 

import argparse
import importlib
from setup import Setup
import data_processing.data_collation as script1
import data_processing.data_cleaning as script2 
import data_processing.poisson as script3 
import data_processing.poisson_per_team as script4

def main(Setup): 
    script1.main(Setup)
    script2.main(Setup)
    script3.main(Setup)
    script4.main(Setup)

if __name__ == "__main__":
     main(Setup)

