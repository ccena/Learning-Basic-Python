# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 18:31:38 2020
One can use np.array to create arrays from Python lists. NumPy is constrained 
to arrays that all contain the same type.
"""
import numpy as np
array_example1 = np.array([1, 4, 2, 5, 3])
print(array_example1)

#Upcasting integers into floating points
array_example2 = np.array([3.14, 4, 2, 3])
print(array_example2)

array_example3 = np.array([1, 2, 3, 4], dtype='float32')
print(array_example3)

# nested lists result in multidimensional arrays
array_example4 = np.array([range(i, i + 3) for i in [2, 4, 6]])
print(array_example4)