import pandas as pd  # For handling data
import matplotlib.pyplot as plt  # For plotting
import seaborn as sns  # For advanced visualization

# Step 1: Load the dataset
# Replace 'your_file.csv' with your actual file name
file_path = "QTL-ToxB-01-30-25.csv"  # CSV file containing QTL data
df = pd.read_csv(file_path)  # Read the CSV file into a Pandas DataFrame

# Step 2: Inspect the dataset structure (Optional, useful for debugging)
print(df.head())  # Show the first five rows to understand the structure

# Step 3: Convert chromosome names to string type to avoid errors
df["Chromosome"] = df["Chromosome"].astype(str)

# Step 4: Determine unique chromosomes and their max positions
chromosomes = df["Chromosome"].unique()  # Get unique chromosome names
chromosome_positions = {chrom: df[df["Chromosome"] == chrom]["Position"].max() for chrom in chromosomes}

# Step 5: Assign numerical values to chromosomes for plotting
chromosome_ticks = {}  # Stores midpoints for chromosome labels
chromosome_start_positions = {}  # Stores starting positions for each chromosome

current_position = 0  # Tracks x-axis positioning
spacing_factor = 10  # Space between chromosomes

for chrom, max_pos in chromosome_positions.items():
    chromosome_start_positions[chrom] = current_position  # Set start position
    chromosome_ticks[chrom] = current_position + max_pos / 2  # Calculate midpoint for labeling
    current_position += max_pos + spacing_factor  # Move to the next chromosome

# Step 6: Map chromosome positions to actual x-axis values
df["Chromosome_Pos"] = df.apply(lambda row: chromosome_start_positions[row["Chromosome"]] + row["Position"], axis=1)

# Step 7: Transform data for plotting
# Convert dataframe from wide to long format for seaborn plotting
df_melted = df.melt(id_vars=["Chromosome", "Position", "Chromosome_Pos"], var_name="Replicate", value_name="LOD Score")

# Step 8: Rename replicate labels for clarity
df_melted["Replicate"] = df_melted["Replicate"].replace({
    "ToxB_Inf_Rep1": "Rep-1",
    "ToxB_Inf_Rep2": "Rep-2",
    "ToxB_Inf_Rep3": "Rep-3",
    "ToxB_Inf_Rep4": "Rep-4"
})

# Step 9: Create the plot
plt.figure(figsize=(16, 6))  # Set figure size

# Define a color palette for distinct replicates
palette = sns.color_palette("husl", n_colors=len(df_melted["Replicate"].unique()))

# Plot LOD scores for each replicate as a line chart
sns.lineplot(data=df_melted, x="Chromosome_Pos", y="LOD Score", hue="Replicate", ci=None, palette=palette, linewidth=2.5)

# Step 10: Add chromosome separator lines
for chrom in chromosome_start_positions.values():
    plt.plot([chrom, chrom], [0.0, 52.0], color="black", linestyle=":", alpha=1, linewidth=1)

# Step 11: Format x-axis and y-axis labels
plt.xlabel("Chromosomes", fontsize=16, fontweight='bold', labelpad=15, color="black")  # X-axis label
plt.ylabel("LOD (STMIM)", fontsize=16, fontweight='bold', labelpad=15, color="black")  # Y-axis label

# Step 12: Adjust tick labels and colors
plt.xticks(list(chromosome_ticks.values()), labels=chromosome_ticks.keys(), rotation=0, fontsize=14, fontweight='bold', color="black")
plt.yticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 52], labels=["0", "5", "10", "15", "20", "25", "30", "35", "40", "45", "", "52"], fontsize=14, fontweight='bold', color="black")

# Step 13: Add threshold line
plt.axhline(y=5, color='red', linestyle='--', linewidth=1.5)  # LOD Threshold at 5

# Step 14: Adjust limits for clarity
plt.ylim(0, 52.0)  # Set y-axis limit
plt.xlim(0, max(df["Chromosome_Pos"]))  # Set x-axis limit

# Step 15: Remove gridlines
plt.grid(False)

# Step 16: Format legend
legend = plt.legend(fontsize=14, title=None, facecolor="white", edgecolor="black", labelcolor="black")
for line in legend.get_lines():
    line.set_linewidth(4)  # Increase legend line thickness

# Step 17: Save the plot as SVG (high quality)
plt.savefig("QTL_Analysis.svg", format="svg", dpi=500, bbox_inches="tight")

# Step 18: Show the plot
plt.show()

# The SVG file will be saved in the current directory
