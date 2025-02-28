import pandas as pd
import numpy as np

# Load the dataset
nba = pd.read_csv("nba_shooting_stats.csv", index_col=0)

# Convert SCORE to binary (1 for missed, 0 for made)
nba['SHOT_RESULT'] = nba['SCORE'].apply(lambda x: 1 if x == 'MISSED' else 0)  # 1 = Missed, 0 = Made

# If RANGE is not available, calculate distance bins
if 'RANGE' not in nba.columns:
    nba['DISTANCE'] = np.sqrt(nba['X']**2 + nba['Y']**2)
    nba['RANGE'] = pd.cut(nba['DISTANCE'], bins=[0, 5, 10, 15, 20, 25, 30], right=False, labels=['0-5 ft', '5-10 ft', '10-15 ft', '15-20 ft', '20-25 ft', '25-30 ft'])

# Group by DEFENDER and RANGE, then calculate success rate
defender_range_success = nba.groupby(['DEFENDER', 'RANGE'])['SHOT_RESULT'].agg(
    total_shots='count',  # Total shots defended in this range
    missed_shots='sum',  # Total shots missed in this range
).reset_index()

# Calculate success rate
defender_range_success['SUCCESS_RATE'] = defender_range_success['missed_shots'] / defender_range_success['total_shots']

# Display the results
print(defender_range_success)

# Find the best defender for each range
best_defender_by_range = defender_range_success.loc[defender_range_success.groupby('RANGE')['SUCCESS_RATE'].idxmax()]

# Display the best defender for each range
print(best_defender_by_range[['RANGE', 'DEFENDER', 'SUCCESS_RATE']])

#Visualization 1

import matplotlib.pyplot as plt
import seaborn as sns

# Plot the best defender for each range
plt.figure(figsize=(10, 6))
sns.barplot(data=best_defender_by_range, x='RANGE', y='SUCCESS_RATE', hue='DEFENDER', palette='viridis')
plt.title("Best Defender by Range")
plt.xlabel("Shot Range")
plt.ylabel("Defender Success Rate")
plt.legend(title='Defender', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

#Visualization 2

# Pivot the data for a heatmap
heatmap_data = defender_range_success.pivot(index='DEFENDER', columns='RANGE', values='SUCCESS_RATE')

# Plot the heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(heatmap_data, annot=True, cmap='viridis', fmt='.2f')
plt.title("Defender Success Rate by Range")
plt.xlabel("Shot Range")
plt.ylabel("Defender")
plt.tight_layout()
plt.show()