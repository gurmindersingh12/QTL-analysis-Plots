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
