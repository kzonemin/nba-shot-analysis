import pandas as pd

# Load the dataset
nba = pd.read_csv("nba_shooting_stats.csv", index_col=0)

# Categorize shots by side of the basket
nba['SIDE'] = nba['X'].apply(lambda x: 'Left' if x < 0 else 'Right')

# Display the first few rows to verify
print(nba[['X', 'SIDE']].head())

# Group by SIDE and calculate FGA, FGM, and FG%
side_stats = nba.groupby('SIDE')['SCORE'].agg(
    FGA='count',  # Total field goal attempts (FGA)
    FGM=lambda x: (x == 'MADE').sum()  # Total field goals made (FGM)
).reset_index()

# Calculate field goal percentage (FG%)
side_stats['FG%'] = side_stats['FGM'] / side_stats['FGA']

# Display the results
print(side_stats)


#Visualization (Bar Plot for FGA and FGM)

import matplotlib.pyplot as plt
import seaborn as sns

# Set up the plot
plt.figure(figsize=(10, 6))

# Plot FGA
sns.barplot(data=side_stats, x='SIDE', y='FGA', color='blue', label='FGA')

# Plot FGM
sns.barplot(data=side_stats, x='SIDE', y='FGM', color='orange', label='FGM', alpha=0.7)

plt.title("Field Goal Attempts (FGA) vs Field Goals Made (FGM) by Side of Basket")
plt.xlabel("Side of Basket")
plt.ylabel("Count")
plt.legend()
plt.tight_layout()
plt.show()
