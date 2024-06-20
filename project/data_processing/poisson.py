"""
This script calculates the probability of each amount of goals scored across all teams. 
It provides funcitons to calculate, print, and plot the probabilities.
"""

import data_processing.data_cleaning as cleaning
import config as configuration
import matplotlib.pyplot as plt
from scipy.stats import poisson

def calculate_probabilities(avg_goals, max_goals=10):
    """
    Calculate Poisson probabilities for a range of goal outcomes.
    """
    poisson_dist = poisson(avg_goals)
    return [poisson_dist.pmf(i) for i in range(max_goals)]

def print_probabilities(home_probs, away_probs):
    """
    Print the probabilities for home and away goals.
    """
    print("Goals Probabilities:")
    for i, (home_prob, away_prob) in enumerate(zip(home_probs, away_probs)):
        print(f"{i} goals: Home: {home_prob:.4f}, Away: {away_prob:.4f}")

def plot_probabilities(home_probs, away_probs):
    """
    Plot the Poisson probabilities for home and away goals.
    """
    x = range(len(home_probs))

    plt.plot(x, home_probs, label='Home Goals', color='red')
    plt.plot(x, away_probs, label='Away Goals', color='blue')

    plt.xlabel('Number of Goals')
    plt.ylabel('Probability')
    plt.title('Probabilities of Home and Away Goal Outcomes')
    plt.xticks(x)
    plt.legend()
    plt.show()


def main(Setup): 
    # Initialize objects in class for use
    home_avg_goals, away_avg_goals, df = cleaning.main(Setup)

    # Calculate probabilities for home and away goals
    home_goals_probs = calculate_probabilities(home_avg_goals)
    away_goals_probs = calculate_probabilities(away_avg_goals)

    # Print the probabilities
    print_probabilities(home_goals_probs, away_goals_probs)

    # Plot the probabilities
    plot_probabilities(home_goals_probs, away_goals_probs)

if __name__ == "__main__":
    Setup = configuration.Setup()
    main(Setup)