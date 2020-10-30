# -*- coding: utf-8 -*-
"""
For even more powerful operations, fancy indexing can be combined with the 
other indexing schemes. 
"""
import numpy as np

# =============================================================================
# All of these indexing options combined lead to a very flexible set of 
# operations for accessing and modifying array values.
# =============================================================================

X = np.arange(12).reshape((3, 4))
print('X: \n', X)
print('Combining Fancy and Simple Indices: ', 
      X[2, [2, 0, 1]])

print('Combining Fancy Indexing with Slicing: \n', X[1:, [2, 0, 1]]) 
#For this example, 1 to 2 is paired with [2,0,1] to access the value

mask = np.array([1, 0, 1, 0], dtype=bool)
row = np.array([0, 1, 2])
print('Combining Fancy Indexing with Masking: \n', X[row[:, np.newaxis], mask])
#For this example, The rows 0, 1, 2 is masked with [True, False, True, False].
#The resulting array only has the columns that are True.

