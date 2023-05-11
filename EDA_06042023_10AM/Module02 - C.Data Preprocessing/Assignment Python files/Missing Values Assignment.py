# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 09:00:10 2023

@author: seema
"""

import pandas as pd
import numpy as np

claimants = pd.read_csv(r"C:\Users\seema\OneDrive\Desktop\COURSE\360DigiTMG Course\EDA_06042023_10AM\Module02 - C.Data Preprocessing\InClass_DataPreprocessing_datasets\Claimants.csv")

claimants

# check for count of NA'sin each column
claimants.isna().sum()

###### There is 1 column that has missing data ---Create an imputer object that fills 'Nan' values of CLMAGE
###### Mean and Median imputer are used for numeric data (CLMAGE)
###### mode is used for discrete (categorical) data 

# for Mean,Meadian,Mode imputation we can use Simple Imputer or df.fillna()

# Mean Imputer 
from sklearn.impute import SimpleImputer

mean_imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
claimants["CLMAGE"] = pd.DataFrame(mean_imputer.fit_transform(claimants[["CLMAGE"]]))
claimants["CLMAGE"].isnull().sum() # 1 record has been  replaced by mean 

claimants.isna().sum()

###### Now, finally our data has no NA values