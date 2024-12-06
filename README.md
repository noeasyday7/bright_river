# bright_river

This repository is created for 02807 Computational Tools for Data Science.

## Overview of the repository's structure

**Notebooks:**

- `I. Data pre-processing.ipynb`: Handles initial data cleaning and preparation.
- `II. Exploratory data analysis.ipynb`: Conducts exploratory data analysis on products data, provides insights into data patterns and distributions.
- `III. Feature-based clustering.ipynb`: Conducts feature extraction, feature scaling, PCA and clustering.
- `IV. Model selection per cluster.ipynb`: Selects appropriate models for each identified cluster.
- `V. Forecasting.ipynb`: Implements forecasting methods to predict future data points.
- `VI. Performance versus Naive Forecast.ipynb`: Compares model performance against a naive forecasting approach.

**Additional Files:**

- `WIP notebooks`: Contains temporary Jupyter notebooks.
- `freq itemsets`: Contains Jupyter notebook used to create frequent itemsets and results.
- `BasicSales.html`: The exploratory data analysis report for products data.
- `parameters.py`: A Python script defining parameters used in model selection per cluster stage.

## Why no dataset

The dataset utilized in this project is derived from Samsøe Samsøe, a Danish fashion brand. The dataset is considered confidential. Access to this dataset is strictly restricted to individuals who have signed a Non-Disclosure Agreement (NDA). This measure ensures the protection of sensitive business information and adheres to privacy and security standards. If you require access to the dataset for review, please contact Maxime Roux (roux@samsoe.com) and complete the NDA process. Unauthorized access or distribution of the dataset is prohibited.

## How to run

Make sure the following Python libraries have been installed:

```python
pandas
numpy
matplotlib
seaborn
ydata_profiling
sklearn
kneed
yellowbrick
tabulate
tsfeatures
scipy
mango
statsmodels
xgboost
tensorflow
itertools
mlxtend
```

Run through all Jupyter notebooks from `I. Data pre-processing.ipynb` to `VI. Performance versus Naive Forecast.ipynb`

