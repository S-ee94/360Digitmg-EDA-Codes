# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 14:55:53 2023

@author: seema
"""

import pandas as pd

seeds = pd.read_csv(r"C:\Users\seema\OneDrive\Desktop\COURSE\360DigiTMG Course\EDA_06042023_10AM\Module02 - C.Data Preprocessing\InClass_DataPreprocessing_datasets\seeds.csv")

seeds

#Standardization
# Normalization function using z std. all are continuous data.
def norm_func(i):
    x = (i-i.mean())/(i.std()) 
    return(x)

seed1_norm = norm_func(seeds)
seed1_norm.describe() # mean=0, std = 1


#Normalization
# or denominator (i.max()-i.min())
def norm_func(i):
    x = (i-i.min())/(i.max()-i.min()) # or denominator (i.max()-i.min())
    return(x)

seed2_norm = norm_func(seeds)
seed2_norm.describe() # min=0, max=1

# We did Standardization and Normalization to make data scale free.
