# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 18:57:14 2023

@author: seema
"""
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

iris = pd.read_csv(r"C:\Users\seema\OneDrive\Desktop\COURSE\360DigiTMG Course\EDA_06042023_10AM\Module02 - C.Data Preprocessing\InClass_DataPreprocessing_datasets\iris.csv")

iris.dtypes

iris.columns

# execute all codes together till legend 
sns.distplot(iris['Sepal.Length'], kde=False,label='Sepal.Length')
sns.distplot(iris['Sepal.Width'], kde=False,label='Sepal.Width')
sns.distplot(iris['Petal.Length'], kde=False,label='Petal.Length')
sns.distplot(iris['Petal.Width'], kde=False,label='Petal.Width')
plt.legend()

# using the binning method of converting the numerical columns to categorical
# 'Sepal.Length'

bins = [1,2,3,4,5,6,7,8]
plt.figure(figsize=(5,4))
sns.set() # light color background
sns.distplot(iris["Sepal.Length"],bins = bins, kde=False)
plt.xticks(bins) # x-axis (1-8)
plt.title("Histogram of Sepal.Length")
plt.show()
iris["Sepal.Length"].value_counts()

# 'Sepal.Width'
bins = [1,2,3,4,5]
plt.figure(figsize=(5,4))
sns.set() # light color background
sns.distplot(iris["Sepal.Width"],bins = bins, kde=False)
plt.xticks(bins) # x-axis (1-8)
plt.title("Histogram of Sepal.Width")
plt.show()
iris["Sepal.Width"].value_counts()

# 'Petal.Length'
bins = [1,2,3,4,5,6,7]
plt.figure(figsize=(5,4))
sns.set() # light color background
sns.distplot(iris["Petal.Length"],bins = bins, kde=False)
plt.xticks(bins) # x-axis (1-8)
plt.title("Histogram of Petal.Length")
plt.show()
iris["Petal.Length"].value_counts()

#'Petal.Width'
bins = [0,1,2,3]
plt.figure(figsize=(5,4))
sns.set() # light color background
sns.distplot(iris["Petal.Width"],bins = bins, kde=False)
plt.xticks(bins) # x-axis (1-8)
plt.title("Histogram of Petal.Widthh")
plt.show()
iris["Petal.Width"].value_counts()



### Discretization Attempt 2

import pandas as pd
import numpy as np

iris = pd.read_csv(r"C:\Users\seema\OneDrive\Desktop\COURSE\360DigiTMG Course\EDA_06042023_10AM\Module02 - C.Data Preprocessing\InClass_DataPreprocessing_datasets\iris.csv")
iris.dtypes

iris.columns

# 'Sepal.Length'
#You can use pd.cut with parameter right = False as:
pd.cut(iris['Sepal.Length'], bins=3, labels=np.arange(3), right=False)

#How the binning is done:
pd.cut(iris['Sepal.Length'], bins=3, right=False)

# 'Sepal.Width'
#You can use pd.cut with parameter right = False as:
pd.cut(iris['Sepal.Width'], bins=3, labels=np.arange(3), right=False)

#How the binning is done:
pd.cut(iris['Sepal.Width'], bins=3, right=False)

# 'Petal.Length'
#You can use pd.cut with parameter right = False as:
pd.cut(iris['Petal.Length'], bins=3, labels=np.arange(3), right=False)

#How the binning is done:
pd.cut(iris['Petal.Length'], bins=3, right=False)

# 'Petal.Width
#You can use pd.cut with parameter right = False as:
pd.cut(iris['Petal.Width'], bins=3, labels=np.arange(3), right=False)

#How the binning is done:
pd.cut(iris['Petal.Width'], bins=3, right=False)

iris


### Discretization Attempt 3

import pandas as pd

df = pd.read_csv(r"C:\Users\seema\OneDrive\Desktop\COURSE\360DigiTMG Course\EDA_06042023_10AM\Module02 - C.Data Preprocessing\InClass_DataPreprocessing_datasets\iris.csv")
df.isnull().sum()
# no null values present in the columns

df.drop_duplicates
#drop duplicate values if any

df.drop(df.columns[[]], axis = 1, inplace = True) 
#drop irrevelant columns for futher analysis
df
#perform discretization/bucketing using pd.cut 
# converting all the continuous columns into discrete categories and categorizing them as low medium high> the categories can be determined further based on the business objective and contraints
df['Slengthdiscrete']=pd.cut(df['Sepal.Length'],3,labels=['low','moderate','high'])

df['Swidthdiscrete']=pd.cut(df['Sepal.Width'],3,labels=['low','moderate','high'])

df['Plengthdiscrete']=pd.cut(df['Petal.Length'],3,labels=['low','moderate','high'])

df['Pwidthdiscrete']=pd.cut(df['Petal.Width'],3,labels=['low','moderate','high'])


df.drop

df.drop(['Sepal.Length','Sepal.Width','Petal.Length','Petal.Width'], axis='columns', inplace=True)
df

# now the conversion of numerical data to categorical is successful



















