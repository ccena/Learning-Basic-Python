# -*- coding: utf-8 -*-
"""
Finding the minimum value and maximum value of any given array
@author: HOTs
"""
import numpy as np
print('Calculating the Min and Max values with max() and min ()')
#Using max and min method
big_array = np.random.rand(1000000)
min_big, max_big = min(big_array), max(big_array)
%timeit min(big_array)
%timeit max(big_array)
print('Min value using min(): ', min_big)
print('Max value using max(): ', max_big)
print('')
#Using np.max and np.min ufunc
print('Calculating the Min and Max values with np.max(), np.min ()')
npmin_big, npmax_big = np.min(big_array), np.max(big_array)
%timeit np.min(big_array)
%timeit np.max(big_array)
print('Min value using ufunc: ', npmin_big)
print('Max value using ufunc: ', npmax_big)
print('')



#NumPy aggregation function will return the aggregate over the entire array
print('Obtaining the Multidimensional Aggregates Along a Row or Column')
M = np.random.random((3, 4))
print('M = ', M)
print('Sum aggregate', np.sum(M)) #Taking the aggregate over the entire array
# The axis keyword specifies the dimension of the array that will be collapsed
print('Min value: ', M.min(axis=0)) #Obtaining the minimum value within 
# each column
print('Max value: ', M.max(axis=1)) #Obtaining the maximum value within 
# each row