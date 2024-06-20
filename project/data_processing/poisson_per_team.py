"""
This script calculates the Poisson distribution of goals scored per team. 
Provides functions to calculate and plot on a graph to compare for all teams.
"""

import data_processing.data_cleaning as cleaning
import pandas as pd
import config as configuration
import matplotlib.pyplot as plt
from scipy.stats import poisson

def calculate_team_poisson_distribution(df):
    """
    Function to calculate every teams Poisson distribution 
    for each number of goals scored per match.
    """
    # Group by HomeTeam and calculate the Poisson distribution for each team
    grouped_data = df.groupby('HomeTeam')
    team_distributions = {}
    for home_team, data in grouped_data:
        average_goals = data['FTHG'].mean()
        team_poisson = poisson(average_goals)
        team_distributions[home_team] = [team_poisson.pmf(i) for i in range(6)]
    return team_distributions

def plot_poisson_distributions(team_distributions):
    """
    A function to plot every team's home Poisson distribution on 1 graph. 
    Used to compare all teams against each other. 
    Output: Shows there isn't much fluctuation between each team.
    """
    x = range(6)
    for home_team, goal_probs in team_distributions.items():
        plt.plot(x, goal_probs, label=home_team)
    
    plt.xlabel('Number of Goals')
    plt.ylabel('Probability')
    plt.title('Poisson Distribution of Goal Outcomes for all Home Teams')
    plt.xticks(x)
    plt.legend()
    plt.show()

def main(Setup):
    # Initialise objects in class for use
    home_avg_goals, away_avg_goals, df = cleaning.main(Setup)
    
    # Calculate Poisson distributions for each team
    team_distributions = calculate_team_poisson_distribution(df)
    
    # Plot Poisson distributions
    plot_poisson_distributions(team_distributions)

if __name__ == "__main__":
    Setup = configuration.Setup()
    main(Setup)