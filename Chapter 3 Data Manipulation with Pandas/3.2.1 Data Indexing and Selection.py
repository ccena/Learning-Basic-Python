# -*- coding: utf-8 -*-
"""
Recall the methods and tools to access, set, and modify values in NumPy arrays.
Indexing ---> (e.g., arr[2, 1]), 
Slicing ---> (e.g., arr[:,1:5]), 
Masking ---> (e.g., arr[arr > 0])
Fancy indexing ---> (e.g., arr[0, [1, 5]])
Combinations thereof ---> (e.g., arr[:, [1, 5]])
"""
# Here we’ll look at similar means of
# accessing and modifying values in Pandas Series and DataFrame objects.
import pandas as pd

message = 'Data Selection in Series'
print(message.upper())
# A Series object acts in many ways like a  one-dimensional NumPy array, 
# and in many ways like a standard Python dictionary.
print('Series as a Dictionary')
data = pd.Series([0.25, 0.5, 0.75, 1.0],
index=['a', 'b', 'c', 'd'])
print('Series Data: ')
print(data)
print('Accessing the data with index b: ', data['b'])
# We can also use dictionary-like Python expressions and methods to examine the
# keys/indices and values:
print('Is there an index "a" in the data?: ', 'a' in data)
print('Index of the data:', data.keys())
print('A list of the index and values of the data: ', list(data.items()))
data['e'] = 1.25 #Adding the data '1.25'with an index e
print('Modified Series Data: ')
print(data)
print('')
# This easy mutability of the objects is a convenient feature: under the hood, 
# Pandas is making decisions about memory layout and data copying that
# might need to take place

print('Series as one-dimensional array')
# A Series builds on this dictionary-like interface and provides array-style 
# item selection such as slices, masking, and fancy indexing.
print('Slicing by explicit index: ')
print(data['a':'c'])

print('Slicing by implicit integer index:')
print(data[0:2])

print('Masking the data: ')
print(data[(data > 0.3) & (data < 0.8)])

print('Fancy Indexing: ')
print(data[['a', 'e']])
print('')

print('Indexers: loc, iloc, and ix: ')
data = pd.Series(['a', 'b', 'c'], index=[1, 3, 5])
print('Data: ')
print(data)
print('Explicit index when indexing, data[1]: ' , data[1])
print('Implicit index when slicing, data[1:3]: ')
print(data[1:3])

# The loc attribute allows indexing and slicing that always references the 
#explicit Python-style index:
print('Indexing using "loc" attribute, data.loc[1]:', data.loc[1] )
print('Indexing using "loc" attribute, data.loc[1:3]: ')
print(data.loc[1:3])


# The iloc attribute allows indexing and slicing that always references the 
# implicit Python-style index:
print('Indexing using "iloc" attribute, data.loc[1]:', data.iloc[1] )
print(data.iloc[1])
print('Indexing using "iloc" attribute, data.loc[1:3]:')
print( data.iloc[1:3])




