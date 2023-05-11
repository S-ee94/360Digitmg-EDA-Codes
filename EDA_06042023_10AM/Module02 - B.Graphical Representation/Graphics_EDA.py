#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 12:57:38 2023

@author: seema
"""

# Data Visualization
# conda install -c conda-forge matplotlib
# pip install matplotlib

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read data into Python
education = pd.read_csv(r"C:\Users\seema\OneDrive\Desktop\COURSE\360DigiTMG Course\EDA_06042023_10AM\DataSets\education.csv")

# Read data into Python
education.shape

# barplot
plt.bar(height = education.gmat, x = np.arange(1, 774, 1)) # initializing the parameter

# Histograms
plt.hist(education.gmat)

plt.hist(education.gmat) # histogram
plt.hist(education.gmat, bins = [600, 680, 710, 740, 780], color = 'green', edgecolor="red") 
plt.hist(education.workex)
plt.hist(education.workex, color='red', edgecolor = "black", bins = 6)

help(plt.hist)

# Histogram using Seaborn
import seaborn as sns
sns.distplot(education.gmat) # Deprecated histogram function from seaborn

sns.displot(education.gmat) # Histogram from seaborn


# Boxplot
plt.figure()
plt.boxplot(education.gmat) # boxplot

help(plt.boxplot)


# Density Plot
sns.kdeplot(education.gmat) # Density plot
sns.kdeplot(education.gmat, bw = 0.5 , fill = True)


# Descriptive Statistics
# describe function will return descriptive statistics includ