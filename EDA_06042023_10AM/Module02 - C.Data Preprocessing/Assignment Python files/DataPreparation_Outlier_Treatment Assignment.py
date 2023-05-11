# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 17:53:42 2023

@author: seema
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

boston = pd.read_csv(r"C:\Users\seema\OneDrive\Desktop\COURSE\360DigiTMG Course\EDA_06042023_10AM\Module02 - C.Data Preprocessing\InClass_DataPreprocessing_datasets\Boston.csv")

boston.info()

# to check the outliers, use boxplot for each and every column 

# crim 
sns.boxplot(boston.crim)
# as per the box plot lot of outliers exist, hence need to remove them using the below techniques


# Detection of outliers (find limits for crim based on IQR)
IQR = boston['crim'].quantile(0.75) - boston['crim'].quantile(0.25)

lower_limit = boston['crim'].quantile(0.25) - (IQR * 1.5)
upper_limit = boston['crim'].quantile(0.75) + (IQR * 1.5)


############### 2. Replace ###############
# Replace the outliers by the maximum and minimum limit
boston['boston_crim'] = pd.DataFrame(np.where(boston['crim'] > upper_limit, upper_limit, np.where(boston['crim'] < lower_limit, lower_limit, boston['crim'])))
sns.boxplot(boston.boston_crim)

# as per the above boxplot now there are no outliers in 'crim' column

# zn column

sns.boxplot(boston.zn)
# as per the box plot lot of outliers exist, hence need to remove them using the below techniques


# Detection of outliers (find limits for zn based on IQR)
IQR = boston['zn'].quantile(0.75) - boston['zn'].quantile(0.25)

lower_limit = boston['zn'].quantile(0.25) - (IQR * 1.5)
upper_limit = boston['zn'].quantile(0.75) + (IQR * 1.5)


############### 2. Replace ###############
# Replace the outliers by the maximum and minimum limit
boston['boston_zn'] = pd.DataFrame(np.where(boston['zn'] > upper_limit, upper_limit, np.where(boston['zn'] < lower_limit, lower_limit, boston['zn'])))
sns.boxplot(boston.boston_zn)

# as per the above boxplot now there are no outliers in 'zn' column

# indus column

sns.boxplot(boston.indus)
# as per the box plot, outliers do not exist hence no need to treat them

#chas
sns.boxplot(boston.chas)
# as per the box plot, outliers do not exist hence no need to treat them

#nox
sns.boxplot(boston.nox)
# as per the box plot, outliers do not exist hence no need to treat them

#rm
sns.boxplot(boston.rm)
# as per the box plot lot of outliers exist, hence need to remove them using the below techniques


# Detection of outliers (find limits for rm based on IQR)
IQR = boston['rm'].quantile(0.75) - boston['rm'].quantile(0.25)

lower_limit = boston['rm'].quantile(0.25) - (IQR * 1.5)
upper_limit = boston['rm'].quantile(0.75) + (IQR * 1.5)


############### 2. Replace ###############
# Replace the outliers by the maximum and minimum limit
boston['boston_rm'] = pd.DataFrame(np.where(boston['rm'] > upper_limit, upper_limit, np.where(boston['rm'] < lower_limit, lower_limit, boston['rm'])))
sns.boxplot(boston.boston_rm)

# as per the above boxplot now there are no outliers in 'rm' column

#age
sns.boxplot(boston.age)
# as per the box plot, outliers do not exist hence no need to treat them

#dis
sns.boxplot(boston.dis)

# as per the box plot lot of outliers exist, hence need to remove them using the below techniques


# Detection of outliers (find limits for dis based on IQR)
IQR = boston['dis'].quantile(0.75) - boston['dis'].quantile(0.25)

lower_limit = boston['dis'].quantile(0.25) - (IQR * 1.5)
upper_limit = boston['dis'].quantile(0.75) + (IQR * 1.5)


############### 2. Replace ###############
# Replace the outliers by the maximum and minimum limit
boston['boston_dis'] = pd.DataFrame(np.where(boston['dis'] > upper_limit, upper_limit, np.where(boston['dis'] < lower_limit, lower_limit, boston['dis'])))
sns.boxplot(boston.boston_dis)

# as per the above boxplot now there are no outliers in 'dis' column

#rad
sns.boxplot(boston.rad)
# as per the box plot, outliers do not exist hence no need to treat them

#tax
sns.boxplot(boston.tax)
# as per the box plot, outliers do not exist hence no need to treat them

#ptratio
sns.boxplot(boston.ptratio)

# as per the box plot lot of outliers exist, hence need to remove them using the below techniques


# Detection of outliers (find limits for ptratio based on IQR)
IQR = boston['ptratio'].quantile(0.75) - boston['ptratio'].quantile(0.25)

lower_limit = boston['ptratio'].quantile(0.25) - (IQR * 1.5)
upper_limit = boston['ptratio'].quantile(0.75) + (IQR * 1.5)


############### 2. Replace ###############
# Replace the outliers by the maximum and minimum limit
boston['boston_ptratio'] = pd.DataFrame(np.where(boston['ptratio'] > upper_limit, upper_limit, np.where(boston['ptratio'] < lower_limit, lower_limit, boston['ptratio'])))
sns.boxplot(boston.boston_ptratio)

# as per the above boxplot now there are no outliers in 'ptratio' column

#black
sns.boxplot(boston.black)

# as per the box plot lot of outliers exist, hence need to remove them using the below techniques


# Detection of outliers (find limits for black based on IQR)
IQR = boston['black'].quantile(0.75) - boston['black'].quantile(0.25)

lower_limit = boston['black'].quantile(0.25) - (IQR * 1.5)
upper_limit = boston['black'].quantile(0.75) + (IQR * 1.5)


############### 2. Replace ###############
# Replace the outliers by the maximum and minimum limit
boston['boston_black'] = pd.DataFrame(np.where(boston['black'] > upper_limit, upper_limit, np.where(boston['black'] < lower_limit, lower_limit, boston['black'])))
sns.boxplot(boston.boston_black)

# as per the above boxplot now there are no outliers in 'black' column

#lstat
sns.boxplot(boston.lstat)

# as per the box plot lot of outliers exist, hence need to remove them using the below techniques


# Detection of outliers (find limits for lstat based on IQR)
IQR = boston['lstat'].quantile(0.75) - boston['lstat'].quantile(0.25)

lower_limit = boston['lstat'].quantile(0.25) - (IQR * 1.5)
upper_limit = boston['lstat'].quantile(0.75) + (IQR * 1.5)


############### 2. Replace ###############
# Replace the outliers by the maximum and minimum limit
boston['boston_lstat'] = pd.DataFrame(np.where(boston['lstat'] > upper_limit, upper_limit, np.where(boston['lstat'] < lower_limit, lower_limit, boston['lstat'])))
sns.boxplot(boston.boston_lstat)

# as per the above boxplot now there are no outliers in 'lstat' column

#medv 
sns.boxplot(boston.medv)

# as per the box plot lot of outliers exist, hence need to remove them using the below techniques


# Detection of outliers (find limits for medv based on IQR)
IQR = boston['medv'].quantile(0.75) - boston['medv'].quantile(0.25)

lower_limit = boston['medv'].quantile(0.25) - (IQR * 1.5)
upper_limit = boston['medv'].quantile(0.75) + (IQR * 1.5)


############### 2. Replace ###############
# Replace the outliers by the maximum and minimum limit
boston['boston_medv'] = pd.DataFrame(np.where(boston['medv'] > upper_limit, upper_limit, np.where(boston['medv'] < lower_limit, lower_limit, boston['medv'])))
sns.boxplot(boston.boston_medv)

# as per the above boxplot now there are no outliers in 'medv' column

# as per the analysis, all outliers have been treated and removed from the respective columns




































