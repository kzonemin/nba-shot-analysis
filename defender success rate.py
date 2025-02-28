import pandas as pd

# Load the dataset
nba = pd.read_csv("nba_shooting_stats.csv", index_col=0)

# Convert SCORE to binary (1 for made, 0 for missed)
nba['SHOT_RESULT'] = nba['SCORE'].apply(lambda x: 0 if x == 'MADE' else 1)  # 1 = Missed, 0 = Made

# Group by DEFENDER and calculate success rate
defender_success = nba.groupby('DEFENDER')['SHOT_RESULT'].agg(
    total_shots='count',  # Total shots defended
    missed_shots='sum',  # Total shots missed while defending
).reset_index()

# Calculate success rate
defender_success['SUCCESS_RATE'] = defender_success['missed_shots'] / defender_success['total_shots']

# Sort by success rate to find the best defender
defender_success_sorted = defender_success.sort_values(by='SUCCESS_RATE', ascending=False)

# Display the results
print(defender_success_sorted)

# Find the best defender
best_defender = defender_success_sorted.iloc[0]
print(f"The best defender is {best_defender['DEFENDER']} with a success rate of {best_defender['SUCCESS_RATE']:.2%}")

#Visualization 
import matplotlib.pyplot as plt
import seaborn as sns

# Plot defender success rates
plt.figure(figsize=(10, 6))
sns.barplot(data=defender_success_sorted, x='DEFENDER', y='SUCCESS_RATE', palette='viridis')
plt.title("Defender Success Rates")
plt.xlabel("Defender")
plt.ylabel("Success Rate (Missed Shots / Total Shots Defended)")
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()