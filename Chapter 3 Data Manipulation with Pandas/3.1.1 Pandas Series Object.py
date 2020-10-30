# -*- coding: utf-8 -*-
"""
A pandas Series has no column labels, as it is just a single column of a 
DataFrame. A Series does have row labels.
"""

import pandas as pd

print('The Pandas Series Object') # Templeate: pd.Series(data, index=index)
# A Pandas Series is a one-dimensional array of indexed data. It can be created
# from a list or array as follows:
data = pd.Series([0.25, 0.5, 0.75, 1.0])
print(data)
print('')
# As we see in the preceding output, the Series wraps both a sequence of values 
# and a sequence of indices, which we can access with the values and index 
# attributes. The values are simply a familiar NumPy array:
print('Values of the data: ', data.values)
# The index is an array-like object of type pd.Index, which we’ll discuss
# in more detail momentarily
print('Index of the Data: ', data.index)

# Like with a NumPy array, data can be accessed by the associated index via
# the familiar Python square-bracket notation:
print('Accessing the second element of the data, data[1]: ', data[1]) 
print('Accessing the second and third element of the data, data[1:3]:')   
print(data[1:3])
print('')
# As we will see, though, the Pandas Series is much more general and flexible 
# than the one-dimensional NumPy array that it emulates

print('Series as Generalized NumPy Array')
# =============================================================================
# The essential difference is the presence of the index: 
# While the NumPy array has an implicitly defined integer index used to access 
# the values, the Pandas Series has an explicitly defined index associated with 
# the values.
# =============================================================================
data = pd.Series([0.25, 0.5, 0.75, 1.0],
                 index = ['a', 'b', 'c', 'd'])
print('Indices of Any Type: ')
print(data)
print("Accessing the second element of the data , data['b']: ", data['b'])
# We can even use noncontiguous or nonsequential indices:
data = pd.Series([0.25, 0.5, 0.75, 1.0],
                 index=[2, 5, 'a', 'b'])
print('Noncontiguous or Nonsequential Indices of Any Type: ')
print(data)
print('')

print( 'Series as Specialized Dictionary')
# The type information of a Pandas Series makes it much more efficient than 
# Python dictionaries for certain operations. 

print( 'Constructing a Series Object directly from a Python Dictionary')
population_dict = {'California': 38332521,
'Texas': 26448193,
'New York': 19651127,
'Florida': 19552860,
'Illinois': 12882135}
print('Dictionary:', population_dict)
population = pd.Series(population_dict)
print('Series Object from a Dictionary: ')
print(population)       
# By default, a Series will be created where the index is drawn from the
# sorted keys. From here, typical dictionary-style item access can be performed
print('Population in California: ', population['California'])
print('Population from California to Illinois: ')
print(population['California':'Illinois'])
print('')

print('Constructing Series objects')
print('Data can be a list or NumPy array!')
pd.Series([2, 4, 6]) #index defaults to an integer sequence
a = pd.Series([2, 4, 6])
print(a) 

print('Data can be a scalar repeated to fill the specified index!')
b = pd.Series(5, index=[100, 200, 300])
print(b)

message ='Data can be a dictionary, where the index defaults to the sorted'
message += ' dictionary keys!'
print(message)
c = pd.Series({2:'a', 1:'b', 3:'c'})
print(c)


print('The index can be explicitly set if a different result is preferred! ')
d = pd.Series({2:'a', 1:'b', 3:'c'}, index=[3, 2])
print(d)
# Notice that in this case, the Series is populated only with the explicitly 
# identified keys.