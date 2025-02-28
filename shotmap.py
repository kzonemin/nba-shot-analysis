#Shot visualization by X,Y

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
nba = pd.read_csv("nba_shooting_stats.csv", index_col=0)

# Create a scatter plot
plt.figure(figsize=(10, 8))

# Use seaborn to plot shots by color and marker style
sns.scatterplot(
    data=nba,
    x='X',
    y='Y',
    hue='SHOOTER',  # Differentiate players by color
    style='SCORE',  # Differentiate made and missed shots by marker style
    palette='viridis',  # Color palette for players
    s=100,  # Marker size
)

# Add court boundaries and labels
plt.xlim(-25, 25)  # Adjust based on your dataset's X range
plt.ylim(0, 50)  # Adjust based on your dataset's Y range
plt.axvline(0, color='black', linestyle='--', linewidth=1)  # Half-court line
plt.title("Shot Locations by different shooters in NBA Playoffs 2021")
plt.xlabel("Horizontal Distance from Basket (ft)")
plt.ylabel("Vertical Distance from Basket (ft)")
plt.legend(title='', bbox_to_anchor=(1.05, 1), loc='upper left')  # Move legend outside the plot

# Show the plot
plt.tight_layout()
plt.show()