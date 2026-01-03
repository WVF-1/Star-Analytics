# Star Analytics: Letting Data Look at the Stars

This project explores how data analytics and light machine learning can uncover natural structure in stellar data — without relying on predefined astronomical labels.

Rather than focusing on prediction or optimization, the goal is curiosity:
**If we let the data observe the stars, what patterns does it discover on its own?**

---

## Project Overview

Stars vary dramatically in temperature, size, brightness, and lifespan. Astronomers have studied these properties for over a century, often visualizing them through tools like the Hertzsprung–Russell diagram.

In this project, we:
- Explore stellar data through **EDA**
- Reduce dimensionality using **PCA**
- Discover natural groupings with **K-Means clustering**
- Interpret clusters as **stellar lifetimes and evolutionary stages**

The emphasis is on interpretability, visualization, and storytelling — not model performance.

---

## Dataset

This project uses the **Star Dataset** from Kaggle, which contains physical properties of stars including:

- Temperature (Kelvin)
- Luminosity (relative to the Sun)
- Radius (relative to the Sun)
- Absolute magnitude
- Star type and color

**Dataset link (CC0 / public):** 
[Kaggle Dataset]([https://www.kaggle.com/datasets/jonassouza872/christmas-hits-daily-streaming-history-2017-2025])).

The dataset is small, clean, and ideal for exploratory analysis and unsupervised learning.

---

## Repository Structure

│
├── data/
│ ├── raw/
│ │ └── Stars.csv
│ └── processed/
│
├── notebooks/
│ ├── 01_eda.ipynb
│ ├── 02_pca_clustering.ipynb
│ └── 03_viz_lifetimes.ipynb
│
├── src/
│ ├── data_processing.py
│ ├── pca_analysis.py
│ └── clustering.py
│
├── reports/
│ └── figures/
│
├── requirements.txt
├── README.md
└── LICENSE


---

## Notebook Guide

### `01_eda.ipynb` — Exploratory Data Analysis
- Feature distributions
- Scale differences across stellar properties
- HR-diagram style visualizations
- Early signs of natural structure

### `02_pca_clustering.ipynb` — PCA & Unsupervised Learning
- Feature scaling
- Dimensionality reduction using PCA
- K-Means clustering in reduced space
- Silhouette score for gentle cluster validation

### `03_viz_lifetimes.ipynb` — Stellar Evolution Interpretation
- Mapping clusters back to physical space
- Temperature vs magnitude (lifecycle view)
- Radius and luminosity comparisons
- Interpreting clusters as evolutionary stages

---

## Methods Used

- Exploratory Data Analysis (EDA)
- Principal Component Analysis (PCA)
- K-Means Clustering
- Silhouette Score (light ML validation)

No hyperparameter tuning or performance optimization was performed — intentionally.

---

## Key Insight

Even without astronomical labels or domain rules, the data naturally organizes itself in ways that reflect real stellar lifetimes and physical laws.

This suggests that **structure is deeply embedded in the data itself**.

---

## Future Work

- Supervised classification of star types
- Feature importance analysis
- Comparison of unsupervised clusters vs labeled classes
- Interactive visualizations

This project is designed as the foundation for a short analytics series.

---

## Requirements

```txt
pandas
numpy
matplotlib
seaborn
scikit-learn
