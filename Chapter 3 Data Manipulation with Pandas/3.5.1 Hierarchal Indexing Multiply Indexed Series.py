# -*- coding: utf-8 -*-
"""
hierarchical
indexing (also known as multi-indexing) to incorporate multiple index levels 
within a single index. In this way, higher-dimensional data can be compactly 
represented within the familiar one-dimensional Series and two-dimensional 
DataFrame objects.
"""
import pandas as pd
import numpy as np

message = 'A Multiply Indexed Series'
print(message.upper())

print('The bad way')
index = [('California', 2000), ('California', 2010),
         ('New York', 2000), ('New York', 2010),
         ('Texas', 2000), ('Texas', 2010)]
populations = [33871648, 37253956, 18976457, 19378102, 20851820, 25145561]
pop = pd.Series(populations, index=index)
print('Series Data:')
print(pop)
print('')
# With this indexing scheme, you can straightforwardly index or slice the series
# based on this multiple index:
print(pop[('California', 2010):('Texas', 2000)])
print(pop[[i for i in pop.index if i[1] == 2010]])
print('This type of data indexing is very inconvenient!!')
print('Although it gives the desired result, it is inefficient for large datasets!')
print('')
print('The Solution: Pandas MultiIndex')
# Pandas MultiIndex type gives us the type of operations we wish to have.
# We can create a multi-index from the tuples as follows:
index = pd.MultiIndex.from_tuples(index) # (index, names=('State', 'Year'))
print(index)
# If we reindex our series with this MultiIndex, we see the hierarchical 
# representation of the data:
pop = pop.reindex(index)
print('Reindexing the Data using MultiIndex:')
print(pop)
# # Now to access all data for which the second index is 2010, we can simply
# # use the Pandas slicing notation
print(pop[:, 2010]) #Slicing notation
print('The result is a singly indexed array with just the keys we’re interested in!')
print('')
# # The unstack() method will quickly convert a multiplyindexed
# Series into a conventionally indexed DataFrame
print('MultiIndex as extra dimension using unstack()')
pop_df = pop.unstack()
print(pop_df)
print('')
# Naturally, the stack() method provides the opposite operation:
print('Using unstack() to go back to the Series Form:')
a = pop_df.stack()
print(a)
print('')
print('Adding Another Column into the DataFrame:')
pop_df = pd.DataFrame({'total': pop,
                       'under18': [9267089, 9284094, 
                                   4687374, 4318033,
                                   5906301, 6879014]})
print(pop_df)

print('Computing the fraction of people under 18 by year:')
f_u18 = pop_df['under18'] / pop_df['total']
print(f_u18.unstack())
print('This allows us to easily and quickly manipulate and explore even high-dimensional data!')









