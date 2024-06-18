import data_processing.data_collation

def predict(home_team, away_team):

    # Calculate the value of lambda (λ) for both Home Team and Away Team.
    if home_team in df_football.index and away_team in df_football.index:
        lambda_home_team = df_football.at[home_team,'GoalsScored'] * df_football.at[away_team,'GoalsConceded']
        lambda_away_team = df_football.at[away_team,'GoalsScored'] * df_football.at[home_team,'GoalsConceded']