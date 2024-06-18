"""
A simple script that pulls in the config.yaml file.
"""

import yaml 

def load_config(file_path='config.yaml'):
    with open(file_path, "r") as file: 
        config = yaml.safe_load(file)
    return config

 