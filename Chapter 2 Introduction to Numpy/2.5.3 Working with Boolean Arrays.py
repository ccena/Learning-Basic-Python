# -*- coding: utf-8 -*-
"""
Given a Boolean array, there are a host of useful operations you can do. 
"""

import numpy as np
import pandas as pd

# use Pandas to extract rainfall inches as a NumPy array
rainfall = pd.read_csv('Seattle2014.csv')['PRCP'].values
inches = rainfall / 254 # 1/10mm -> inches

print('Counting Entries')
rng = np.random.RandomState(0)
y = rng.randint(10, size=(3, 4))
print('y = \n', y)
print('Values that are less than 6: \n', np.less(y, 6))
print('Total values that are less than 6: ' , np.count_nonzero(y < 6))
print('Total values that are less than 6: ' , np.sum(y < 6))
#This counts the number of values less than 6 in each row of the matrix.
print('Total values in each row less than 6: ', np.sum(y < 6, axis=1)) 
print('Are there values greater than 8? ', np.any(y > 8))
print('Are there values less than 0? ', np.any(y < 0))
print('Are all values less than 10? ', np.any(y < 10))
print('Are all values equal to 6? ', np.all(y == 6))
# np.all() and np.any() can be used along particular axes as well
print('Are all values in each row less than 8? ', np.all(y < 8, axis=1))
print('')

print('Boolean operators')
message = 'Days where rainfall is between 0.5 and 1.0 inches:'
print(message, np.sum((inches > 0.5) & (inches < 1)))
# =============================================================================
#bitwise Boolean operators and their equivalent ufuncs    
#    &     np.bitwise_and
#    |     np.bitwise_or
#    ^     np.bitwise_xor
#    ~     np.bitwise_not
# =============================================================================

# Here are some examples of results we can compute when combining
# masking with aggregations:    
print("Number days without rain: ", np.sum(inches == 0))
print("Number days with rain: ", np.sum(inches != 0))
print("Days with more than 0.5 inches:", np.sum(inches > 0.5))
print("Rainy days with < 0.1 inches :", np.sum((inches > 0) & (inches < 0.2)))