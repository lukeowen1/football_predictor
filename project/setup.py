""" 
Stores any setup functions such as loading config.
"""

import config as configuration
import pandas as pd 

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.options.mode.chained_assignment = None

class Setup: 

    def __init__self(): 
        self.config = configuration.load_config()   