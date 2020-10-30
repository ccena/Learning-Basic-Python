# -*- coding: utf-8 -*-
"""
A more powerful pattern is to use Boolean arrays as masks, to select particular
subsets of the data themselves.
"""

#Suppose we want an array of all values in the array that are less than 5:
import numpy as np
import pandas as pd

# use Pandas to extract rainfall inches as a NumPy array
rainfall = pd.read_csv('Seattle2014.csv')['PRCP'].values
inches = rainfall / 254 # 1/10mm -> inches
rng = np.random.RandomState(0)
y = rng.randint(10, size=(3, 4))
print('y = \n', y)
print('Total values that are less than 5: \n' , y < 5)
# Now to select these values from the array, we can simply index on this Boolean 
# array; this is known as a masking operation:
print('All values that are less than 5: ', y[y < 5]) #Masking Operation
print('')
# construct a mask of all rainy days
rainy = (inches > 0)
# construct a mask of all summer days (June 21st is the 172nd day)
summer = (np.arange(365) - 172 < 90) & (np.arange(365) - 172 > 0)
print("Median precip on rainy days in 2014 (inches): ",
np.median(inches[rainy]))
print("Median precip on summer days in 2014 (inches): ",
np.median(inches[summer]))
print("Maximum precip on summer days in 2014 (inches): ",
np.max(inches[summer]))
print("Median precip on non-summer rainy days (inches):",
np.median(inches[rainy & summer]))