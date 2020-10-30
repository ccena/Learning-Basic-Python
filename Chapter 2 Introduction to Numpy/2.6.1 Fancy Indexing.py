# -*- coding: utf-8 -*-
"""
One can access and modify portions of arrays using simple indices 
(e.g., arr[0]), slices (e.g., arr[:5]), and Boolean masks (e.g., arr[arr> 0]).
Fancy indexing is like the simple indexing we’ve already seen, but we pass
arrays of indices in place of single scalars. This allows us to very quickly 
access and modify complicated subsets of an array’s values.
"""
import numpy as np

print('Exploring Fancy Indexing')
print('')
rand = np.random.RandomState(42)
x = rand.randint(100, size=10)
print('x: ', x)
ind1= [3, 7, 4]
print('Accessing elements, [x[3], x[7], x[2]]: ', x[ind1])
ind2 = np.array([[3, 7],
          [4, 5]])
print('Creating an Array from the Indexed Elements:\n', x[ind2]) 
#the shape of the result reflects the shape of the index arrays rather than 
# the shape of the array being indexed:
print('')
print('Fancy Indexing in Multiple Dimensions')
X = np.arange(12).reshape((3, 4))
print(X)
row = np.array([0, 1, 2])
col = np.array([2, 1, 3])
print('Creating an Array from the Indexed Elements: ', X[row, col])
# first value in the result is X[0, 2], the second is X[1, 1], and the
# third is X[2, 3].
print('')

print('row:\n', row[:, np.newaxis])
print('col: ', col)
print('Broadcasting Example,  row[:, np.newaxis] * col: \n',
      row[:, np.newaxis] * col)
print('Creating a 2D Array from Broadcasted Indexed Elements: \n',
      X[row[:, np.newaxis], col])

# It is always important to remember with fancy indexing that the return value 
# reflects the broadcasted shape of the indices, rather than the shape of the 
# array being indexed.