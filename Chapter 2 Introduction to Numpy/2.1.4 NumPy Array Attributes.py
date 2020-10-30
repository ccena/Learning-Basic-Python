# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 20:13:52 2020
This is an example of Numpy's random number generator to create 
random-valued arrays. The seed function allows the same value to be 
generated in each array during every run.
"""
import numpy as np
np.random.seed(0) 
x1 = np.random.randint(10, size=6) # One-dimensional array
x2 = np.random.randint(10, size=(3, 4)) # Two-dimensional array
x3 = np.random.randint(10, size=(3, 4, 5)) # Three-dimensional array

print(x1)
print('\n')
print(x2)
print('\n')
print(x3) 
print('\n')

#Attributes of an Array
print("x3 ndim: ", x3.ndim) #Number of dimensions
print("x3 shape:", x3.shape) #Size f each dimension
print("x3 size: ", x3.size) #Total size of the array
print("dtype:", x3.dtype) #Gives the data type of the array
print("itemsize:", x3.itemsize, "bytes") #Size (in bytes) of each array
print("nbytes:", x3.nbytes, "bytes") #Product of itemsize and size