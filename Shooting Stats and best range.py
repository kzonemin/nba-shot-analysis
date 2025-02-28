#Most shots made by range

import pandas as pd

# Load the dataset
nba = pd.read_csv("nba_shooting_stats.csv", index_col=0)

# Calculate the shooting percentage for each player and range
nba['SHOT_RESULT'] = nba['SCORE'].apply(lambda x: 1 if x == 'MADE' else 0)  # Convert 'MADE' to 1, 'MISSED' to 0
shooting_percentage = nba.groupby(['SHOOTER', 'RANGE'])['SHOT_RESULT'].mean().reset_index()

# Find the range with the highest shooting percentage for each player
best_range = shooting_percentage.loc[shooting_percentage.groupby('SHOOTER')['SHOT_RESULT'].idxmax()]

# Display the result
print(best_range[['SHOOTER', 'RANGE', 'SHOT_RESULT']])