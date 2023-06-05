import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the Excel file
data = pd.read_excel("Assignment_Dataset.xlsx", sheet_name="Sheet1")

# Access the necessary columns
date = data["Date"]
pr = data["PR"]
ghi = data["GHI"]

# Calculate the moving average of PR using a window of 30 days
moving_average = pr.rolling(window=30).mean()

# Calculate the budget line values dynamically based on the year
current_year = date.dt.year.max()
budget_line = 73.9 - (current_year - date.dt.year) * 0.8

# Set the colors for the scatter plot based on GHI values
colors = np.where(ghi < 2, "navy", np.where(ghi < 4, "lightblue", np.where(ghi < 6, "orange", "brown")))

# Create the figure and axes
fig, ax = plt.subplots()

# Plot the scatter points with colored shading based on GHI
ax.scatter(date, pr, color=colors, label="PR", alpha=0.7)

# Plot the moving average of PR as a red line
ax.plot(date, moving_average, color="red", label="30-d Moving Avg")

# Plot the budget line as a dark green line
ax.plot(date, budget_line, color="darkgreen", label="Budget Line")

correlation_coefficient = data["GHI"].corr(data["PR"])
print("Correlation Coefficient:", correlation_coefficient)

# Set the labels and title
ax.set_xlabel("Date")
ax.set_ylabel("PR")
ax.set_title("Performance Evolution")

# Add a legend
ax.legend()

# Show the plot
plt.show()
