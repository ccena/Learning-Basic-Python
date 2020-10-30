# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 18:50:26 2020

@author: HOTs
"""
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn; seaborn.set() # set plot style

# We use pandas to read the file and extract the height information
data = pd.read_csv('president_heights.csv') #The data gives the order, name
# and height of each president
heights = np.array(data['height(cm)']) #Extracting the height data from file
print(heights)
# name = np.array(data['name'])
# print(name)
print('')
print('Obtained Quantities from the Height of every US President')
print("Mean height: ", heights.mean())
print("Standard deviation:", heights.std())
print("Minimum height: ", heights.min())
print("Maximum height: ", heights.max())
print("25th percentile: ", np.percentile(heights, 25))
print("Median: ", np.median(heights))
print("75th percentile: ", np.percentile(heights, 75))


plt.hist(heights) #Creating a distribution of the height
plt.title('Height Distribution of US Presidents')
plt.xlabel('height (cm)')
plt.ylabel('number')