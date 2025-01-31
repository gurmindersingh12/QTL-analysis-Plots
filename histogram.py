# Import required libraries
import pandas as pd  # For handling and processing tabular data
import matplotlib.pyplot as plt  # For plotting the histograms

# ------------------------ STEP 1: Load the dataset ------------------------
# Define the file path (you can change this to the path where your CSV is stored)
file_path = "kg.csv"

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# Display the first few rows of the dataset to understand its structure
print(df.head())

# ------------------------ STEP 2: Data Cleaning ------------------------
# The dataset has four replicates (Rep1, Rep2, Rep3, Rep4) containing numerical values.
# However, they might be stored as strings. We need to convert them to numeric values.

# Define the replicate columns
rep_cols = ["Rep1", "Rep2", "Rep3", "Rep4"]

# Convert replicate columns to numeric (if they contain non-numeric values, they will be converted to NaN)
df[rep_cols] = df[rep_cols].apply(pd.to_numeric, errors='coerce')

# Check if there are any missing values in the dataset
print(df.isnull().sum())

# We found that some values were missing (NaN). However, in this case, we will not fill them.
# Instead, we proceed with visualization.

# ------------------------ STEP 3: Set up the Plot ------------------------
# We will create a 2x2 grid of histograms, where each subplot represents a replicate.

# Define a 2x2 figure layout
fig, axes = plt.subplots(2, 2, figsize=(12, 10), dpi=300)  # figsize controls the size of the figure

# Titles for each subplot
rep_titles = ["Rep-1", "Rep-2", "Rep-3", "Rep-4"]

# Define colors for the histograms (one unique color per replicate)
colors = ["blue", "green", "red", "purple"]

# Define bin edges for the phenotypic scale (0 to 3, divided into 0.5 intervals)
bins = [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]

# ------------------------ STEP 4: Plot Histograms ------------------------
# We use a loop to create four subplots (one for each replicate)

for i, ax in enumerate(axes.flat):  # 'axes.flat' flattens the 2x2 array into a 1D array for easy looping
    rep_col = rep_cols[i]  # Get the replicate column name
    counts, bins, patches = ax.hist(df[rep_col], bins=bins, edgecolor="black", alpha=0.7, color=colors[i])

    # Add labels on top of each bar
    for count, bin_edge in zip(counts, bins[:-1]):  # Iterate through bin counts and edges
        ax.text(bin_edge + 0.25, count + 1, str(int(count)), ha='center', fontsize=12, color='black')

    # Set the title for each subplot
    ax.set_title(rep_titles[i], fontsize=14, fontweight='bold')  # Bold title

    # Label the x-axis and y-axis
    ax.set_xlabel("Phenotypic Scale", fontsize=12, fontweight='bold')  # Bold x-axis title
    ax.set_ylabel("Number of RILs", fontsize=12, fontweight='bold')  # Bold y-axis title

    # Set tick marks for the x-axis to match phenotypic scale values
    ax.set_xticks(bins)

    # Set y-axis from 0 to 70 with intervals of 10
    ax.set_yticks(range(0, 71, 10))
    ax.set_ylim(0, 70)  # Fix y-axis range for consistency across all plots

    # Add cross marks (tick marks) for better readability
    ax.tick_params(axis='x', direction='inout', length=6, width=2)
    ax.tick_params(axis='y', direction='inout', length=6, width=2)

    # Remove gridlines for a cleaner look
    ax.grid(False)

# ------------------------ STEP 5: Save and Display the Plot ------------------------
# Adjust layout to prevent overlapping
plt.tight_layout()

# Define the file path to save the figure as an SVG file
svg_file_path = "phenotypic_distribution.svg"

# Save the figure in SVG format (high-quality vector format)
plt.savefig(svg_file_path, format="svg", dpi=300)

# Show the figure
plt.show()

# Print the file path where the figure is saved
print(f"Plot saved successfully as: {svg_file_path}")
