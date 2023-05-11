# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 14:41:07 2023

@author: seema
"""

# Zero Variance

# Python Libraries (Packages)
import pandas as pd

# Read data into Python
Z_data = pd.read_csv(r"C:\Users\seema\OneDrive\Desktop\COURSE\360DigiTMG Course\EDA_06042023_10AM\Module02 - C.Data Preprocessing\InClass_DataPreprocessing_datasets\Z_Dataset.csv")
Z_data

Z_data.dtypes

print(Z_data['square.length'].var())
print(Z_data['square.breadth'].var())
print(Z_data['rec.length'].var())
print(Z_data['rec.breadth'].var())
print(Z_data['Id'].var())

# 'square.length' , 'square.breadth', 'rec.length ', 'rec.breadth ' are the columns that have zero variance 
      
# hence using the xero variance method we usually ignore the columns with zero variance data preprocessing technique     
