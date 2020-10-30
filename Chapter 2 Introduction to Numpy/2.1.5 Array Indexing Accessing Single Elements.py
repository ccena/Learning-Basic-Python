# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 21:02:19 2020
Array indexing in Numpy involves specifying the desired index 
in square brackets to access the ith value starting from zero.
"""
import numpy as np
np.random.seed(0) #allows the same value to be generated in 
# each array during every run.
x = np.random.randint(10, size=(3, 4)) # Two-dimensional array
print(x)
print('\n')
print(x[:2], '-- subarray: first row up to second row elements')
print('\n')
print(x[1:3], '-- subarray: second row up to last row elements')
print('\n')
print(x[:, 1:2], '-- subarray: only the second column elements')
print('\n')
print(x[2: , 0:3], '-- subarray: third row, three columns')
print('\n')
print(x[2,1], '-- third row, second column')
print(x[2,3],'-- thrid row, last column')
print(x[0,0],'-- first row, first column')
print(x[0,-1],'-- first row, last column')
print(x[-2,-1],'-- second row, last column')