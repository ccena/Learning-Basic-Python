# -*- coding: utf-8 -*-
"""
The most straightforward way to construct a multiply indexed Series or DataFrame
is to simply pass a list of two or more index arrays to the constructor.
"""
import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.rand(4, 2),
index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
columns=['data1', 'data2'])
print('DataFrame created using a list of indexed arrays:')
print(df)
print('')

# Similarly, if you pass a dictionary with appropriate tuples as keys, 
# Pandas will automatically recognize this and use a MultiIndex by default:

print('Series Data with Tuples as Keys:')
data = {('California', 2000): 33871648,
('California', 2010): 37253956,
('Texas', 2000): 20851820,
('Texas', 2010): 25145561,
('New York', 2000): 18976457,
('New York', 2010): 19378102}
print(pd.Series(data))

message = 'Explicit MultiIndex constructors'
print(message.upper())
print('Creating MultiIndex from a simple list of arrays:')
print(pd.MultiIndex.from_arrays([['a', 'a', 'b', 'b'], [1, 2, 1, 2]]))
print('Creating MultiIndex from a list of tuples:')
print(pd.MultiIndex.from_tuples([('a', 1), ('a', 2), ('b', 1), ('b', 2)]))
print('Creating MultiIndex from a Cartesian product of single indices:')
print(pd.MultiIndex.from_product([['a', 'b'], [1, 2]]))
print('Creating MultiIndex using its internal encoding by passing levels and labels:')
print(pd.MultiIndex([['a', 'b'], [1, 2]],
            [[0, 0, 1, 1], [0, 1, 0, 1]],  names = ('Index', 'Frequency')))
index = pd.MultiIndex([['a', 'b'], [1, 2]],
            [[0, 0, 1, 1], [0, 1, 0, 1]], names = ('Index', 'Frequency'))
print('')
populations = [33871648, 37253956, 18976457, 19378102]
pop = pd.DataFrame({'populations': populations}, index=index)
pop = pop.reindex(index)
print(pop)

print('')
print('MultiIndex for columns')
# hierarchical indices and columns
index = pd.MultiIndex.from_product([[2013, 2014], [1, 2]],
names=['year', 'visit'])
columns = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'], 
                            ['HR', 'Temp']], names=['subject', 'type'])

# mock some data
data = np.round(np.random.randn(4, 6), 1)
data[:, ::2] *= 10
data += 37
# create the DataFrame
health_data = pd.DataFrame(data, index=index, columns=columns)
print('Health Data:')
print(health_data)
print('Accessing a Guido\'s Health Data:')
print(health_data.Guido)

