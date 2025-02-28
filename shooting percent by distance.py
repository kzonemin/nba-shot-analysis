import pandas as pd
import numpy as np

# Load the dataset
nba = pd.read_csv("nba_shooting_stats.csv", index_col=0)

# If RANGE is not available, calculate distance from basket using X and Y
nba['DISTANCE'] = np.sqrt(nba['X']**2 + nba['Y']**2)

# Convert SCORE to binary (1 for made, 0 for missed)
nba['SHOT_RESULT'] = nba['SCORE'].apply(lambda x: 1 if x == 'MADE' else 0)

# Group by distance (or RANGE) and calculate shooting percentage
if 'RANGE' in nba.columns:
    shooting_percentage = nba.groupby('RANGE')['SHOT_RESULT'].mean().reset_index()
else:
    # Bin distances into ranges (e.g., 0-5 ft, 5-10 ft, etc.)
    nba['DISTANCE_BIN'] = pd.cut(nba['DISTANCE'], bins=[0, 5, 10, 15, 20, 25, 30], right=False)
    shooting_percentage = nba.groupby('DISTANCE_BIN')['SHOT_RESULT'].mean().reset_index()

# Display the shooting percentage by distance
print(shooting_percentage)

#Visualization 

import matplotlib.pyplot as plt
import seaborn as sns

# Plot shooting percentage by distance
plt.figure(figsize=(10, 6))
if 'RANGE' in nba.columns:
    sns.barplot(data=shooting_percentage, x='RANGE', y='SHOT_RESULT', palette='viridis')
else:
    sns.barplot(data=shooting_percentage, x='DISTANCE_BIN', y='SHOT_RESULT', palette='viridis')

plt.title("Shooting Percentage by Distance from Basket")
plt.xlabel("Distance from Basket (ft)")
plt.ylabel("Shooting Percentage")
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()