# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 14:34:40 2023

@author: seema
"""

'''
Q1) Calculate Skewness, and Kurtosis using Python code & draw inferences on the following data. Refer to the Datasets attachment for the data file.
Hint: [Insights drawn from the data such as data is normally distributed/not, outliers, measures like mean, median, mode, variance, std. deviation]

'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cars = pd.read_csv(r"C:\Users\seema\OneDrive\Desktop\COURSE\360DigiTMG Course\EDA_06042023_10AM\DataSets\cars.csv")

cars.info()

# Third moment business decision / Skewness

cars.speed.skew() # skewness is negative(<0)
cars.dist.skew() # skewness is positive(>0)


# Fourth moment business decision

cars.speed.kurt()  # kurtosis is negative(<3)
cars.dist.kurt()   # kurtosis is negative(<3)

# b. Top Speed (SP) and Weight (WT)

cars1 = pd.read_csv(r"C:\Users\seema\OneDrive\Desktop\COURSE\360DigiTMG Course\EDA_06042023_10AM\DataSets\cars1.csv")

cars1.info()
# Third moment business decision / Skewness

cars1.SP.skew() # skewness is negative(<0)
cars1.WT.skew() # skewness is negative(<0)


# Fourth moment business decision

cars1.SP.kurt()  # kurtosis is negative(<3)
cars1.WT.kurt()   # kurtosis is negative(<3)


'''
Q3) Below are the scores obtained by a student on tests 
[34,36,36,38,38,39,39,40,40,41,41,41,41,42,42,45,49,56]
1)	Find the mean, median, variance, and standard deviation.
2)	What can we say about the student marks? [Hint: Looking at the various measures calculated above whether the data is normal/skewed or if outliers are present].  
'''


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

a = np.array([34,36,36,38,38,39,39,40,40,41,41,41,41,42,42,45,49,56])
b = pd.Series(a)

b.mean()
b.median()
b.var()
b.std()

plt.figure()
plt.boxplot(b)

'''
(iii)	Suppose that the above histogram and the boxplot in question 2 are plotted for the same dataset. Explain how these graphs complement each other in providing information about any dataset. Hint: [Visualizing both the plots, draw the insights]
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cars = pd.read_csv(r"C:\Users\seema\OneDrive\Desktop\COURSE\360DigiTMG Course\EDA_06042023_10AM\DataSets\cars.csv")

cars.info()

plt.figure()
plt.hist(cars.speed)
plt.boxplot(cars.speed)


















