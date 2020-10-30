# -*- coding: utf-8 -*-
"""
NumPy has fast built-in aggregation functions for working on arrays such as
the sum, product, median, minimum and maximum, quantiles, etc.
"""
import numpy as np
np.random.seed(0)

# Summing the Values in an Array
print('Comparing the Calculation Time of sum() and np.sum()')
#Comparing the efficiency of sum() and np.sum()
big_array = np.random.rand(1000000)
%timeit sum(big_array) #sum() method does not apply to multidimensional arrays
%timeit np.sum(big_array) #np.sum() ufunc is aware of multiple array dimensions
print('Using sum method: ', sum(big_array))
print('Using sum ufunc: ', big_array.sum()) #np.sum(big_array) can be written as big_array.sum()
print('')





