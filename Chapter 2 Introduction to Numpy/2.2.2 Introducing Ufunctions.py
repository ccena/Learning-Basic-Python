# -*- coding: utf-8 -*-
"""
NumPy provides a convenient interface into just this
kind of statically typed, compiled routine known as a vectorized operation.
One can accomplish this by simply performing an operation on the array,
which will then be applied to each element.
"""
import numpy as np
#Exploring NumPy’s UFuncs
print('Flexible Scalar-Vector and Vector-Vector Operations')
print(5/np.arange(1, 6)) #Dividing a scalar by an array
print('')
print(np.arange(5)*np.arange(1, 6)) #Holds true for arrays of the same size
print('')
print(np.arange(5)/np.arange(1, 6)) #Holds true for arrays of the same size
print('')
x = np.arange(9).reshape((3, 3)) #Holds true for multidimensional arrays
y = 2 ** x #Computations are more efficient than those using functions
print(y)

