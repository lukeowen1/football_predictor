
<h3 align="center">Football_Predictor</h3>

  <p align="left">
    This repository contains scripts and notebooks for downloading, processing, and analysing the last 10 seasons of Premier League data to form predictions.
    <br />

<!-- ABOUT THE PROJECT -->
## Made With

[![forthebadge](http://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com)
  
## Repository Structure
```plaintext
football_predictor/
│
├── project/
│   ├── data_processing/
│        ├── data_collation.py
│        ├── data_cleaning.py
│        ├── poisson.py
│        ├── poisson_per_team.py
│   ├── config.py
│   ├── config.yaml 
│   ├── main.py
│   ├── setup.py    
│
│── requirements.txt
└── README.md

```
<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Installation

1. Clone the repository via terminal
   ```sh
   git clone https://github.com/lukeowen1/football_predictor/
   ```
3. Use the terminal to create a virtual environment
   ```sh
   python -m venv venv
   ```
4. Activate the virtual environment
   ```sh
   source venv/bin/activate
   ```
5. Install pip / check the latest version is running
   ```sh
   python3 -m pip install --upgrade pip
   python3 -m pip --version
   ```
6. Install external packages and libraries
   ```sh
   pip install -r requirements.txt
   ```


<!-- USAGE EXAMPLES -->

## How to use the repository 

This repository is designed to be used from the terminal, however each script can be ran separately if desired / testing. 

If wanting to replicate this project, you will have to update the `csv_file_path` paths in the `config.yaml` file with your path to the CSVs. 

```yaml

data_collation: 
    csv_file_path: /Users/lwowen/Library/CloudStorage/OneDrive-Deloitte(O365D)/Documents/prem_league_data/*.csv

```

### How the scripts are structured

There are 4 scripts that together do the collation, cleaning and analysing of the data using Poisson distributions. All these scripts are ran sequentially from the `main.py` script: 
```sh
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
```
### How to run the scripts
Simply run `python3 main.py` in the terminal to run each script sequentially. Scripts can be commented out in the `main.py` script for development and testing.

## Coming Soon
This project is still in progress, with a lot of different statistical analysis methods left to trial. Also, there are many Machine Learning methods that will be applied and experimented on this data, such as Random Forest Classification, Linear Regression, Logistic Regression and K-Means Clustering to name the most relevant.

If you have any ideas on anything else that can be added, please do let me know or create a branch!

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
