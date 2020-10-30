# -*- coding: utf-8 -*-
"""
Both the Series and DataFrame objects contain an  explicit index lets you
reference and modify data. This Index object is an interesting structure in 
itself, and it can be thought of either as an immutable array or as an ordered 
set
"""

import pandas as pd
print('INDEX AS IMMUTABLE ARRAY')
# As a simple example, let’s construct an Index from a list of integers
ind = pd.Index([2, 3, 5, 7, 11])
print('Indices: ', ind)

# The Index object in many ways operates like an array. For example, we can use 
# standard Python indexing notation to retrieve values or slices:
print('Value of the 2nd index: ', ind[1])
print('Value of every other index: ', ind[::2])
# Index objects also have many of the attributes familiar from NumPy arrays:
print('Index Attributes: ', ind.size, ind.shape, ind.ndim, ind.dtype)
print('')
# =============================================================================
# Note: One difference between Index objects and NumPy arrays is that indices 
# are immutable—that is, they cannot be modified via the normal means:
# ind[1] = 0 does not change the value of the index to zero
# =============================================================================

print('INDEX AS ORDERED SET')
# Pandas objects are designed to facilitate operations such as joins across 
# datasets, which depend on many aspects of set arithmetic.
indA = pd.Index([1, 3, 5, 7, 9])
indB = pd.Index([2, 3, 5, 7, 11])
print('Index A and Index B: ', indA , indB)
print('Intersection of A and B: ', indA & indB) #Finds the similarities of the indices
print('Union of A and B: ', indA | indB) #Combines the indices
#and unifies the intersection between them
print('Symmetric Difference between A and B: ', indA ^ indB) #Subtracts the 
# intersection from the union of the indices