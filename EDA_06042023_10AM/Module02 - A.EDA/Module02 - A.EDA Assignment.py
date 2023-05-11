"""
Created on Wed Apr 12 15:45:28 2023

@author: seema
"""

# Q1) Calculate Mean, and Standard Deviation using Python code & draw inferences on the following data. 
# Refer to the Datasets attachment for the data file.
# Hint: [Insights drawn from the data such as data is normally distributed/not, outliers, measures like mean, 
# median, mode, variance, std. deviation]

import pandas as pd
import numpy as np 
cars = pd.read_csv(r"C:\Users\seema\COURSE\360DigiTMG Course\EDA_06042023_10AM\DataSets\cars.csv")

cars.info()

# Measures of Central Tendency / First moment business decision

cars.speed.mean()
cars.dist.mean()

cars.speed.median()
cars.dist.median()

cars.speed.mode()
cars.dist.mode()

# Measures of Dispersion / Second moment business decision

cars.speed.var()
cars.dist.var()

cars.speed.std()
cars.dist.std()

range_speed = max(cars.speed) - min(cars.speed)
range_speed

range_dist = max(cars.dist) - min(cars.dist)
range_dist

# Third Moment Business Decision / Skewness 

cars.speed.skew() # skew is negative(<0) hence negatively skewed
cars.dist.skew()  # skew is positive(>0) hence positively skewed

# Fourth Moment Business Decision / Kurtosis

cars.speed.kurt() # kurt is less than 3 hence negative kurtosis
cars.dist.kurt()  # kurt is less than 3 hence negative kurtosis


# To detect outliers using boxplot
import matplotlib.pyplot as plt

plt.figure()
plt.boxplot(cars.speed)  # no outliers as per the boxplot visualization
plt.boxplot(cars.dist) # there are outliers visible as per boxplot visualization

help(plt.boxplot)

# b) Top Speed (SP) and Weight (WT)

cars1 = pd.read_csv(r"C:\Users\seema\OneDrive\Desktop\COURSE\360DigiTMG Course\EDA_06042023_10AM\DataSets\cars1.csv")

cars1.info()

# Measures of Central Tendency / First moment business decision

cars1.SP.mean()
cars1.WT.mean()

cars1.SP.median()
cars1.WT.median()

cars1.SP.mode()
cars1.WT.mode()

# Measures of Dispersion / Second moment business decision

cars1.SP.var()
cars1.WT.var()

cars1.SP.std()
cars1.WT.std()

range_SP = max(cars1.SP) - min(cars1.SP)
range_SP

range_WT = max(cars1.WT) - min(cars1.WT)
range_WT

# Third Moment Business Decision / Skewness 

cars1.SP.skew() # skew is negative(<0) hence negatively skewed
cars1.WT.skew()  # skew is positive(>0) hence positively skewed

# Fourth Moment Business Decision / Kurtosis

cars1.SP.kurt() # kurt is less than 3 hence negative kurtosis
cars1.WT.kurt()  # kurt is less than 3 hence negative kurtosis


# To detect outliers using boxplot
import matplotlib.pyplot as plt

plt.figure()
plt.boxplot(cars1.SP)  # no outliers as per the boxplot visualization
plt.boxplot(cars1.WT) # there are outliers visible as per boxplot visualization

'''
Q2) Below are the scores obtained by a student on tests. 
34, 36, 36, 38, 38, 39, 39, 40, 40, 41, 41, 41, 41, 42, 42, 45, 49, 56
1)	Find the mean, median and mode, variance, and standard deviation.
2)	What can we say about the student marks? 
3)	What can you say about the Excepted value for the student score?

'''

# 1) 
# Measures of Central Tendency / First moment business decision

stu_scores = pd.read_csv(r"C:\Users\seema\OneDrive\Desktop\COURSE\360DigiTMG Course\EDA_06042023_10AM\DataSets\student_scores.csv")

stu_scores.scores.mean()
stu_scores.scores.median()
stu_scores.scores.mode()

# Measures of Dispersion / Second moment business decision
stu_scores.scores.var()
stu_scores.scores.std()


# Third Moment Business Decision / Skewness 

stu_scores.scores.skew() # skew is positive(>0) hence positively skewed


# Fourth Moment Business Decision / Kurtosis

stu_scores.scores.kurt() # kurt is greater than 3 hence positive kurtosis

# plotting the density/probability distribution plot to find insights on student marks
import seaborn as sns
sns.kdeplot(stu_scores.scores, bw = 0.5 , fill = True)

# Insights on Expected Value for the Student Score

# As per the density plot the expected value is the mean of the student score which is 41.0.

'''

Q7) Calculate Mean, Median, Mode, Variance, Standard Deviation, and Range & comment about 
the values / draw inferences, for the given dataset.
-	For Points, Score, Weigh>
Find Mean, Median, Mode, Variance, Standard Deviation, and Range and comment on the 
values/ Draw some inferences. 

Dataset: Refer to Hands-on Material in LMS - Data Types EDA assignment snapshot of the 
dataset is given above.

'''

sports = pd.read_csv(r"C:\Users\seema\OneDrive\Desktop\COURSE\360DigiTMG Course\EDA_06042023_10AM\DataSets\sports.csv")

sports.info()

# Measures of Central Tendency / First moment business decision

sports.Points.mean()
sports.Score.mean()
sports.Weight.mean()

sports.Points.median()
sports.Score.median()
sports.Weight.median()

sports.Points.mode()
sports.Score.mode()
sports.Weight.mode()

# Measures of Dispersion / Second moment business decision

sports.Points.var()
sports.Score.var()
sports.Weight.var()

sports.Points.std()
sports.Score.std()
sports.Weight.std()


range_Points = max(sports.Points) - min(sports.Points)
range_Points

range_Score= max(sports.Score) - min(sports.Score)
range_Score

range_Weight = max(sports.Weight) - min(sports.Weight)
range_Weight

'''
Q9) Look at the data given below. Plot the data, find the outliers, and find out: 
μ,σ,σ^2
Hint: [Use a plot that shows the data distribution, and skewness along with the outliers;
also use Python code to evaluate measures of centrality and spread]

'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

company = pd.read_csv(r"C:\Users\seema\OneDrive\Desktop\COURSE\360DigiTMG Course\EDA_06042023_10AM\DataSets\company.csv")
# -*- coding: utf-8 -*-

company.info()

# as per the above information Measure column is an object type hence converting the
# same to float in order to calculate mean

company.Measure = company.Measure.str.replace('%', '').astype(float)

# Measures of Central Tendency / First moment business decision

company.Measure.mean()

# Measures of Dispersion / Second moment business decision

company.Measure.var()
company.Measure.std()

# Box plot to show outliers,distribution of numerical data and skewness

plt.figure()
plt.boxplot(company.Measure,vert=False)

#Insights ->
# As per the box plot analysis, There are outliers in the Measure_X data of the
# company dataset, The skewness is positive and hence data is positively distributed

























