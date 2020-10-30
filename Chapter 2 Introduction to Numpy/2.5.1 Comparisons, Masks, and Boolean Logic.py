# -*- coding: utf-8 -*-
"""
This section covers the use of Boolean masks to examine and manipulate
values within NumPy arrays. Masking comes up when you want to extract, modify, 
count, or otherwise manipulate values in an array based on some criterion. 
In NumPy, Boolean masking is often the most efficient way to accomplish 
these types of tasks.
"""
import pandas as pd
import matplotlib.pyplot as plt

# use Pandas to extract rainfall inches as a NumPy array
rainfall = pd.read_csv('Seattle2014.csv')['PRCP'].values
inches = rainfall / 254 # 1/10mm -> inches

%matplotlib inline
import matplotlib.pyplot as plt
import seaborn; seaborn.set() # set plot styles
plt.hist(inches, 40); 
# =============================================================================
# This histogram gives us a general idea that the vast majority of days in 
# Seattle saw near zero measured rainfall in 2014. However, this does not 
# answer the following: 
# How many rainy days were there in the year? 
# What is the average precipitation on those rainy days?
# How many days were there with more than half an inch of rain?
# =============================================================================

# =============================================================================
# One approach to this would be to answer these questions by hand: loop through
# the data, incrementing a counter each time we see values in some desired 
# range. For reasons discussed throughout this chapter, such an approach is 
# very inefficient, both from the standpoint of time writing code and time 
# computing the result.
# =============================================================================
