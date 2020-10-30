# -*- coding: utf-8 -*-
"""
Broadcasting is simply a set of rules for applying binary ufuncs 
(addition, subtraction, multiplication, etc.) on arrays of different sizes.
"""
import numpy as np

print('Adding Arrays of Similar Sizes')
a = np.array([0, 1, 2])
b = np.array([5, 5, 5])
print('a + b = ', a + b) #Adding arrays of similar sizes
print('')

# Broadcasting allows these types of binary operations to be performed on 
# arrays of different sizes
print('Broadcasting a scalar to an array')
print('a + 5 = ', a + 5) 
print('')

# A one-dimensional array 'a' is stretched, or broadcast, across the second
# dimension in order to match the shape of 'M'
print('Broadcasting a one-dimensional array to a two-dimensional array:')
M = np.ones((3, 3))
print('M + a = \n', M + a)
print('')

# More complicated cases can involve broadcasting of both arrays
print('Broadcasting both array:')
c = np.arange(3)
d = np.arange(3)[:, np.newaxis]
print('c = ', c)
print('')
print('d = \n', d)
print('')
print('c + d = \n', c + d)