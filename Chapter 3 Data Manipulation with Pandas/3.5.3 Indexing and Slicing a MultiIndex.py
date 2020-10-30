# -*- coding: utf-8 -*-
"""
Indexing and slicing on a MultiIndex is designed to be intuitive, and it
helps if you think about the indices as added dimensions.
"""

import pandas as pd
import numpy as np

print('Multiply indexed Series')
index = [('California', 2000), ('California', 2010),
         ('New York', 2000), ('New York', 2010),
         ('Texas', 2000), ('Texas', 2010)]
populations = [33871648, 37253956, 18976457, 19378102, 20851820, 25145561]
pop = pd.Series(populations, index=index)
index = pd.MultiIndex.from_tuples(index, names=('State', 'Year'))
pop = pop.reindex(index)
print(pop)
print('We can access (California,2000) data by indexing with multiple terms:')
print(pop['California', 2000])

# The MultiIndex also supports partial indexing, or indexing just one of the 
# levels in the index.
print('We can access California data by partial indexing:')
print(pop['California'])
print('Partial slicing is available as well, as long as the MultiIndex is sorted')
print(pop.loc['California':'New York']) # pop.iloc[0:2] #pop.loc[:'New York']
# With sorted indices, we can perform partial indexing on lower levels by 
# passing an empty slice in the first index:
print('Indexing on the lower levels using empty slices in the 1st index:')
print(pop[:, 2000])
print('Selection based on Boolean Mask:')
print(pop[pop > 22000000])
print('Selection based on Fancy Indexing:')
print(pop[['California', 'Texas']])
print('')

print('Multiply Indexed DataFrames')
# A multiply indexed DataFrame behaves in a similar manner.
index = pd.MultiIndex.from_product([[2013, 2014], [1, 2]],
names=['year', 'visit'])
columns = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'], 
                            ['HR', 'Temp']], names=['subject', 'type'])

data = np.round(np.random.randn(4, 6), 1)
data[:, ::2] *= 10
data += 37
health_data = pd.DataFrame(data, index=index, columns=columns)
print('Health Data:')
print(health_data)
print('')
print('Guido\'s Temperature Data:')
print(health_data['Guido', 'Temp'])#Slicing Guido's temperature data'
print('')
print('Bob\'s HR and Temperature Data using .loc[]:')
print(health_data.iloc[:2, :2])
print('')
# These indexers provide an array-like view of the underlying two-dimensional 
# data, but each individual index in loc or iloc can be passed a tuple of 
# multiple indices.
print('Bob\'s HR Data using .loc[] and tuple of indices:')
print(health_data.loc[:, ('Bob', 'HR')])
print('')
# You could get around this by building the desired slice explicitly
# By using the IndexSlice object.
idx = pd.IndexSlice
print('Accessing patient\'s HR Data using IndexSlice:')
print(health_data.loc[idx[:, 1], idx[:, 'HR']]) #Slicing the row with a value 
# of 1 and a column with HR data.

