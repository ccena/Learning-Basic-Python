# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 22:46:57 2020
The reshape method() is a convenient, flexible way of reshaping an array
"""
import numpy as np

grid = np.arange(1, 10).reshape((3, 3)) # size of the initial array must match
#the size of the reshaped array
print(grid)
print('\n')
x = np.array([1, 2, 3])
# row vector via reshape
print(x.reshape((1, 3)))
print('\n')

# row vector via newaxis
print(x[np.newaxis, :])
print('\n')

# column vector via reshape
print(x.reshape((3, 1)))
print('\n')

# column vector via newaxis
print(x[:, np.newaxis])