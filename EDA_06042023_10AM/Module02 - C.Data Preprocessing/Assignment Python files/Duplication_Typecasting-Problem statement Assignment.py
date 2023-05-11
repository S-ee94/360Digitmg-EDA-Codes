# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 18:44:16 2023

@author: seema
"""

import pandas as pd
import numpy as np

OnlineRetail = pd.read_csv(r"C:\Users\seema\OneDrive\Desktop\COURSE\360DigiTMG Course\EDA_06042023_10AM\Module02 - C.Data Preprocessing\InClass_DataPreprocessing_datasets\OnlineRetail.csv")

print(OnlineRetail.head())

'''Q1. For the given dataset perform the type casting (convert the datatypes, ex. float to int)"

################## Type casting###############################################

'''

OnlineRetail.dtypes
#type casting
# Now we will convert 'float64' into 'int64' type.

OnlineRetail.UnitPrice = OnlineRetail.UnitPrice.astype('int64')
OnlineRetail.UnitPrice.dtypes

# now the column 'UnitPrice' dtype has been converted to int64 

"Error while converting CustomerID(float64) to (int64)"
"Cannot convert non-finite values (NA or inf) to integer"
"1ts we have to fill NA values"

from sklearn.impute import SimpleImputer

# Mean Imputer 
mean_imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
OnlineRetail["CustomerID"] = pd.DataFrame(mean_imputer.fit_transform(OnlineRetail[["CustomerID"]]))
OnlineRetail["CustomerID"].isnull().sum()  # all 2 records replaced by mean 

# Now we will convert 'float64' into 'int64' type. 
OnlineRetail['CustomerID'] = OnlineRetail['CustomerID'].astype('int64') 
OnlineRetail['CustomerID'].dtypes

"Q2. Check for the duplicate values, and handle the duplicate values (ex. drop)"

#Identify duplicates records in the data
duplicate = OnlineRetail.duplicated()
sum(duplicate) # 5284

#Removing Duplicates
data1 = OnlineRetail.drop_duplicates() 

"Q3. Do the data analysis (EDA)?"
"Such as histogram, boxplot, scatterplot etc "

#Graphical Representation
import matplotlib.pyplot as plt # mostly used for visualization purposes 
# import numpy as np


#Quantity
plt.hist(OnlineRetail.Quantity);plt.show() #histogram

plt.boxplot(OnlineRetail.Quantity);plt.show() #boxplot


#UnitPrice
plt.hist(OnlineRetail.UnitPrice);plt.show() #histogram

plt.boxplot(OnlineRetail.UnitPrice);plt.show() #boxplot

#CustomerID
plt.hist(OnlineRetail.CustomerID);plt.show() #histogram

plt.boxplot(OnlineRetail.CustomerID);plt.show() #boxplot


#Scatter plot

plt.scatter(x=OnlineRetail.Quantity,y=OnlineRetail.UnitPrice)
plt.show()

plt.scatter(x=OnlineRetail.CustomerID,y=OnlineRetail.UnitPrice)
plt.show()















