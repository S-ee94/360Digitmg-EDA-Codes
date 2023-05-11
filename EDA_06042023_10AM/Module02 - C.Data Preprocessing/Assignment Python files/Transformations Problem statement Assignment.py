# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 09:22:08 2023

@author: seema
"""

import pandas as pd
import matplotlib.pyplot as plt

calories_consumed = pd.read_csv(r"C:\Users\seema\OneDrive\Desktop\COURSE\360DigiTMG Course\EDA_06042023_10AM\Module02 - C.Data Preprocessing\InClass_DataPreprocessing_datasets\calories_consumed.csv")
calories_consumed

#Normal Quantile-Quantile Plot

import scipy.stats as stats
import pylab

# Checking Whether data is normally distributed

stats.probplot(calories_consumed['Weight_gained_in_gms'], dist='norm',plot=pylab);plt.show() #pylab is visual representation
# The above QQ plot for 'Weight_gained_in_gms' column is not normally distributed
##### So the data is not normal we have to transform it to normal

stats.probplot(calories_consumed['Calories_consumed'], dist='norm',plot=pylab);plt.show() 
# it is normally distributed for 'Calories_consumed' column



#transformation to make 'Weight_gained_in_gms' variable normal
import numpy as np

#applying log transformation
stats.probplot(np.log(calories_consumed['Weight_gained_in_gms']),dist="norm",plot=pylab) #best transformation method

calories_consumed.describe() #transformation has been applied to the dataset

# now both variables are normally distributed