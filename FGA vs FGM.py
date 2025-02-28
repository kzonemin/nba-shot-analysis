import pandas as pd
import numpy as np

# Load the dataset
nba = pd.read_csv("nba_shooting_stats.csv", index_col=0)

# If RANGE is not available, calculate distance bins
if 'RANGE' not in nba.columns:
    nba['DISTANCE'] = np.sqrt(nba['X']**2 + nba['Y']**2)
    nba['RANGE'] = pd.cut(nba['DISTANCE'], bins=[0, 5, 10, 15, 20, 25, 30], right=False, labels=['0-5 ft', '5-10 ft', '10-15 ft', '15-20 ft', '20-25 ft', '25-30 ft'])

# Group by RANGE and calculate FGA and FGM
range_stats = nba.groupby('RANGE')['SCORE'].agg(
    FGA='count',  # Total field goal attempts (FGA)
    FGM=lambda x: (x == 'MADE').sum()  # Total field goals made (FGM)
).reset_index()

# Calculate field goal percentage (FG%)
range_stats['FG%'] = range_stats['FGM'] / range_stats['FGA']

# Display the results
print(range_stats)

#Visualization (Bar Plot for FGA and FGM)
import matplotlib.pyplot as plt
import seaborn as sns

# Set up the plot
plt.figure(figsize=(12, 6))

# Plot FGA
sns.barplot(data=range_stats, x='RANGE', y='FGA', color='blue', label='FGA')

# Plot FGM
sns.barplot(data=range_stats, x='RANGE', y='FGM', color='orange', label='FGM', alpha=0.7)

plt.title("Field Goal Attempts (FGA) vs Field Goals Made (FGM) per Range")
plt.xlabel("Shot Range")
plt.ylabel("Count")
plt.legend()
plt.tight_layout()
plt.show()

#Visualization (Line Plot for FG%)
# Set up the plot
plt.figure(figsize=(10, 6))

# Plot FG%
sns.lineplot(data=range_stats, x='RANGE', y='FG%', marker='o', color='green', label='FG%')

plt.title("Field Goal Percentage (FG%) per Range")
plt.xlabel("Shot Range")
plt.ylabel("Field Goal Percentage")
plt.ylim(0, 1)  # Set y-axis limits to 0-100%
plt.tight_layout()
plt.show()
