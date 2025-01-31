# 📊 Phenotypic & QTL Data Visualization

This repository contains Python scripts for **visualizing phenotypic trait distributions** and **QTL analysis results**. The scripts generate high-quality **SVG plots** that are useful for genetic analysis, trait mapping, and publications.

---

## 📌 Features
✅ **Phenotypic Data Visualization**:
- Creates **2x2 histograms** to visualize phenotypic trait distributions across four replicates.
- Uses **custom colors, labeled bars, and high-resolution output**.
- **Removes gridlines** for a clean and professional appearance.
- **Cross marks (ticks) on axes** for better numerical readability.

✅ **QTL Analysis Visualization**:
- Generates a **LOD score plot** across chromosomes to identify significant QTLs.
- Uses **separate colors for each replicate**.
- **Adds threshold lines** for significant QTL detection.
- **Chromosome-wise separation lines** to clearly distinguish markers.
- **Formatted x-axis & y-axis with bold labels** for clarity.

---

## 📂 File Structure
📁 QTL-and-Phenotypic-Visualization │── 📄 kg.csv # Input file for phenotypic data visualization │── 📄 QTL-ToxB-01-30-25.csv # Input file for QTL analysis visualization │── 📄 plot_phenotypic_histograms.py # Python script for phenotypic visualization │── 📄 plot_qtl_analysis.py # Python script for QTL LOD score visualization │── 📄 phenotypic_distribution.svg # Output visualization (phenotypic histograms) │── 📄 QTL_Analysis.svg # Output visualization (QTL LOD plot) │── 📄 README.md # Documentation (you are here)


---

## 🛠️ Installation & Setup
### **1️⃣ Install Required Libraries**
Ensure you have **Python 3.x** installed. Then, install the required libraries:

```bash
pip install pandas matplotlib seaborn

🚀 Running the Scripts
Phenotypic Data Visualization

    Ensure your dataset (kg.csv) is in the same directory.
    Run the script:

python plot_phenotypic_histograms.py

✅ Output: A high-quality phenotypic_distribution.svg file.
QTL Analysis Visualization

    Ensure your QTL dataset (QTL-ToxB-01-30-25.csv) is in the same directory.
    Run the script:

python plot_qtl_analysis.py

✅ Output: A high-quality QTL_Analysis.svg file.
🖼️ Example Outputs
Phenotypic Data Histogram

(Replace with an actual link if hosted online.)
QTL LOD Score Plot

(Replace with an actual link if hosted online.)
📊 Understanding the Visualizations
1️⃣ Phenotypic Data Histograms

    X-axis: Phenotypic scale (ranges from 0 to 3, in 0.5 increments).
    Y-axis: Number of RILs in each phenotypic category.
    Custom Colors: Different colors for each replicate.
    Labels: Count of RILs displayed on each bar.
    No Gridlines: Clean appearance.

2️⃣ QTL Analysis LOD Score Plot

    X-axis: Chromosome positions (adjusted for visualization).
    Y-axis: LOD (Likelihood of Detection) scores.
    Threshold Line: A red dashed line at LOD = 5 to indicate significance.
    Chromosome Separators: Vertical dashed lines to differentiate chromosomes.
    Legend: Color-coded replicates for clarity.

🔄 Modifications & Customization

Want to tweak the visualizations?
Phenotypic Data

    Change colors → Modify colors in plot_phenotypic_histograms.py.
    Adjust bin size → Modify the bins list.
    Save as PNG/PDF → Change "svg" to "png" or "pdf" in plt.savefig().

QTL Analysis

    Change threshold → Adjust plt.axhline(y=5, ...) in plot_qtl_analysis.py.
    Modify x-axis scaling → Adjust spacing_factor in the chromosome processing section.
    Save as PNG/PDF → Change "svg" to "png" or "pdf" in plt.savefig().

📝 License

This project is licensed under the MIT License – feel free to use, modify, and share it.
👨‍💻 Author

Developed by [Your Name]
