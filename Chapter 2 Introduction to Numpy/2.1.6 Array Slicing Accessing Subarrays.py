# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 22:20:22 2020
To access subarrays, one can use the slice notation marked by the colon 
(:) character.
"""
import numpy as np

#One Dimensional Array
print('Accessing Elements of a Onedimensional Array')
x = np.arange(10)
print(x)
print('\n')
print(x[:5]) # first five elements
print('\n')
print(x[5:]) # elements after index 5
print('\n')
print(x[4:7]) # middle subarray
print('\n')
print(x[::2]) # every other element
print('\n')
print(x[1::2]) # every other element, starting at index 1
print('\n')
print(x[::-1]) # all elements, reversed
print('\n')
print(x[5::-2]) # reversed every other from index 5
print('\n')

#Multidimensional subarrays
print('Accessing Elements of a Multidimensional Array')
np.random.seed(0)
x2 = np.random.randint(10, size=(3, 4)) # Two-dimensional array
print(x2)
print('\n')
print(x2[:2, :3]) # two rows, three columns
print('\n')
print(x2[:3, ::2]) # all rows, every other column
print('\n')
print(x2[::-1, ::-1]) # reversing the subarray dimensions
print('\n')

# Accessing array rows and columns
print('Accessing Array Rows and Colums of a Multidimensional Array')
print(x2[:, 0]) # first column of x2
print('\n')
print(x2[0, :]) # first row of x2
print('\n')
print(x2[0]) # equivalent to x2[0, :]
print('\n')

# Subarrays as no-copy views
print('Modifying the Values in an Array')
# Array slices return views rather than copies of the array data
x2_sub = x2[:2, :2]
print(x2_sub)
print('\n')
x2_sub[0, 0] = 100 # modifying the first element of the subarray
print(x2_sub)
print('\n')
print(x2)
print('\n')

# Creating copies of arrays
print('Using Copy() method to Create Copies of an Array')
x2_sub_copy = x2[:2, :2].copy()
print(x2_sub_copy)
print('\n')
x2_sub_copy[0, 0] = 42
print(x2_sub_copy)
print('\n')
print(x2)