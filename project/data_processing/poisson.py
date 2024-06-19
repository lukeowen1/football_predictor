""" 
This script applies the Poisson distribution to our values. This gives the probability 
for each amount of goals scored by the home & away team and visualises it. 
"""

import data_processing.data_cleaning as cleaning
import pandas as pd 
import config as configuration
import matplotlib.pyplot as plt
from scipy.stats import poisson

def main(Setup): 

    # initialise objects in class for use
    home_avg_goals, away_avg_goals, df = cleaning.main(Setup)

    # Define the Poisson distributions for home and away goals
    home_poisson = poisson(home_avg_goals)
    away_poisson = poisson(away_avg_goals)

    # Generate probabilities for different goal outcomes
    home_goals_probs = [home_poisson.pmf(i) for i in range(10)]
    away_goals_probs = [away_poisson.pmf(i) for i in range(10)]

    # Print the probabilities for different goal outcomes
    print("Home Goals Probabilities:")
    for i, prob in enumerate(home_goals_probs):
        print(f"{i} goals: {prob:.4f}")

    print("\nAway Goals Probabilities:")
    for i, prob in enumerate(away_goals_probs):
        print(f"{i} goals: {prob:.4f}")


    # Plot the probabilities
    x = range(10)

    plt.plot(x, home_goals_probs, label='Home Goals', color='red')
    plt.plot(x, away_goals_probs, label='Away Goals', color='blue')

    plt.xlabel('Number of Goals')
    plt.ylabel('Probability')
    plt.title('Probabilities of Home and Away Goal Outcomes')
    plt.xticks(x)
    plt.legend()
    plt.show()


   







