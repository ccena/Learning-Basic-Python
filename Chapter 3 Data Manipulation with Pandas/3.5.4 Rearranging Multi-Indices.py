# -*- coding: utf-8 -*-
"""
One of the keys to working with multiply indexed data is knowing how to effectively
transform the data. There are more ways to finely control the rearrangement of data
between hierarchal indices and columns aside from stack() and unstack().
"""


import pandas as pd
import numpy as np

print('Many of the MultiIndex slicing operations will fail if the index is not sorted.')
index = pd.MultiIndex.from_product([['a', 'c', 'b'], [1, 2]])
data = pd.Series(np.random.rand(6), index=index)
data.index.names = ['char', 'int']
print('Series Data:' )
print(data)
print('Error occurs when doing data[\'a\':\'b\'] since the data is not sorted!')
# For various reasons, partial slices and other similar operations
# require the levels in the MultiIndex to be in sorted
print('')
# Pandas provides a number of convenience routines to perform sorting;
# such as sort_index() and sortlevel() methods of the DataFrame.
print('Sorting the index using sort_index():')
data = data.sort_index()
print(data)
print('With the sorted index, we can now obtain the partial slice of the data:')
print(data['a':'b'])
print('')

print('Stacking and unstacking indices')
# It is possible to convert a dataset from a stacked multi-index
# to a simple two-dimensional representation optionally specifying the level 
# to use:
index = [('California', 2000), ('California', 2010),
         ('New York', 2000), ('New York', 2010),
         ('Texas', 2000), ('Texas', 2010)]
populations = [33871648, 37253956, 18976457, 19378102, 20851820, 25145561]
pop = pd.Series(populations, index=index)
index = pd.MultiIndex.from_tuples(index, names=('State', 'Year'))
pop = pop.reindex(index)
print(pop)
print('Unstacking at level 0:')
print(pop.unstack(level=0))
print('Unstacking at level 1:')
print(pop.unstack(level=1))
print('')
# The opposite of unstack() is stack(), which here can be used to recover 
# the original series:
print('Recovering the original data using stack()')
print(pop.unstack().stack())
print('')

print('Index setting and resetting using reset_index method:')
# Another way to rearrange hierarchical data is to turn the index labels into
# columns; this can be accomplished with the reset_index method
pop_flat = pop.reset_index(name='population')
print(pop_flat)

print(pop_flat.set_index(['State', 'Year']))

