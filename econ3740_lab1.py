# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""
Introduction to Econometrics - Lab 1
Instructor: [Your Name]
Course: Intro to Econometrics (using Wooldridge)

This lab introduces Python basics and data handling 
with pandas, numpy, and statsmodels.
"""

# =========================================================
# 1. Installing and Importing Libraries
# =========================================================
# To install packages (uncomment and run):
# pip install pandas numpy statsmodels

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf

# =========================================================
# 2. Basic Math in Python
# =========================================================

# Arithmetic
4 / 2    # division
4 + 2    # addition
4 - 2    # subtraction
4 * 2    # multiplication

# Using numpy for math functions
np.log(4)    # natural logarithm

# =========================================================
# 3. Variables
# =========================================================
a = 1
a == 1       # True (comparison)
# Note: variable names cannot start with a number
1 = 2-1
1 == 2-1

# =========================================================
# 4. Indexing in Python
# =========================================================
# In Python, indexing starts at 0 (not 1 as in math).
# We use square brackets [] to select elements.

# Example with a simple list:
numbers = [10, 20, 30, 40]

numbers[0]    # first element → 10
numbers[1]    # second element → 20
numbers[-1]   # last element → 40

# =========================================================
# 5. Reading Data
# =========================================================
# Load data from CSV or Excel
data = pd.read_csv("data.csv")
# data = pd.read_excel("data.xlsx")

# =========================================================
# 6. Exploring Data
# =========================================================
data                # display dataset
data.describe()     # summary statistics
data.info()         # dataset info
data.head()         # first 5 rows
data.tail()         # last 5 rows
data.shape          # dimensions (rows, columns)
data.columns        # column names

# =========================================================
# 7. Selecting Columns
# =========================================================
data["math4"]                     # single column
data[["math4", "read4"]]        # multiple columns

# =========================================================
# 8. Basic Statistics
# =========================================================
data["math4"].max()
data["math4"].min()
data["math4"].mean()
data["math4"].std()

# Sort by a column
data.sort_values(by="math4", ascending=False)

# Frequency counts
data["math4"].value_counts()
data["math4"].value_counts().sort_values()
data["math4"].value_counts().sort_index()

# Cross-tabulation
pd.crosstab(data["female"], data["married"])
pd.crosstab(data["female"], data["married"], normalize="columns")
pd.crosstab(data["female"], data["married"], normalize="index")

# =========================================================
# 9. Filtering Data
# =========================================================
# Select rows where math4 = 100
data[data["math4"] == 100]

# Using AND / OR in filters
data[(data["math4"] > 90) | (data["read4"] == 100)]

# Correlation between two variables
data["read4"].corr(data["math4"])

# =========================================================
# 10. Data Management
# =========================================================
# Drop a column
data = data.drop(columns=["read4"])

# Create a new variable
data["read4_20"] = data["read4"] / 5

# Unique values in a column
data["read4"].unique()

# =========================================================
# 11. Simple Regression
# =========================================================
# Estimate wage on experience
model = smf.ols("wage ~ exper", data=data)
results = model.fit()
print(results.summary())

# =========================================================
# 12. (Optional) Wooldridge Datasets
# =========================================================
# To install wooldridge datasets:
# pip install wooldridge
# import wooldridge as woo
# data = woo.data("wage1")
# data = pd.read_stata("file.dta")



