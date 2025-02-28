# NBA Shot Analysis: Player Performance, Defender Impact, and Court Positioning (2021 Playoffs)

![NBA Visualization Example](https://example.com/path/to/image.png) <!-- Add an image if you have one -->

This project analyzes NBA shooting statistics from the 2021 playoffs to uncover insights into player performance, defender effectiveness, and shot distribution across the court. Using Python and data visualization libraries, the project explores key metrics such as **Field Goal Attempts (FGA)**, **Field Goals Made (FGM)**, and **Field Goal Percentage (FG%)** by range and side of the basket. It also evaluates defender success rates and identifies the best defenders.

---

## Table of Contents
1. [Dataset](#dataset)
2. [Analysis](#analysis)
3. [Key Insights](#key-insights)
4. [How to Run the Code](#how-to-run-the-code)
5. [Results](#results)
6. [Visualizations](#visualizations)
7. [License](#license)

---

## Dataset
The dataset (`nba_players_shooting.csv`) contains the following columns:
- `SHOOTER`: Name of the player taking the shot.
- `X`, `Y`: Horizontal and vertical distance of the shot from the basket (in feet).
- `RANGE`: Radius range of the shot (e.g., 0-5 ft, 5-10 ft).
- `DEFENDER`: Name of the player defending the shot.
- `SCORE`: Whether the shot was made (`MADE`) or missed (`MISSED`).

---

## Analysis
The project focuses on three main areas of analysis:
1. **Shooting Efficiency by Range**:
   - Calculates FGA, FGM, and FG% for each shot range (e.g., 0-5 ft, 5-10 ft).
   - Determines the range at which players are most efficient.

2. **Defender Impact**:
   - Evaluates defender success rates (percentage of shots missed when defended).
   - Identifies the best defenders and their effectiveness in different ranges.

3. **Court Positioning**:
   - Compares FGA, FGM, and FG% from the left vs. right side of the basket.
   - Analyzes whether players perform differently based on court positioning.

---

## Key Insights
- **Shooting Efficiency**: Players are more likely to score closer to the basket, with FG% decreasing as shot distance increases.
- **Best Defenders**: Russell Westbrook has the highest success rate, forcing misses on almost 75% of defended shots.
- **Court Positioning**: Shots from the left side of the basket have a similar FG% to shots from the right side, indicating no significant bias.

---

## How to Run the Code
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/nba-shot-analysis.git

2. Install the required libraries:
   ```bash
   pip install pandas matplotlib seaborn numpy

3. Run the Python script
   ```bash
    python nba_shot_stats.py

### Results
The analysis reveals:
Players are most efficient in the 0-5 ft range, with an FG% of [X]%.
The best defender is [Defender Name], with a success rate of [X]%.
Shots from the left side of the basket have an FG% of [X]%, compared to [X]% from the right side.

### Visualizations
The project includes the following visualizations:

1. Shooting Efficiency by Range:
a) Bar plots showing FGA and FGM by range.
b) Line plot showing FG% trends across ranges.

2. Defender Success Rate:
a) Bar plot of the best defenders by success rate.
b) Heatmap of defender success rates by range.

3. Court Positioning:
a) Bar plots comparing FGA and FGM from the left vs. right side of the basket.

License
This project is licensed under the MIT License. See the LICENSE file for details.

### Acknowledgments
Dataset: https://www.nba.com/stats/players/shooting?Season=2020-21&SeasonType=Playoffs&PerMode=Totals
Libraries: pandas, matplotlib, seaborn, numpy
