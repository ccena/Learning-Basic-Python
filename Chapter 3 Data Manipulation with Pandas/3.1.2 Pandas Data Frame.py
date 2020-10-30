# -*- coding: utf-8 -*-
"""
A DataFrame is a 2-dimensional data structure that can store data of 
different types (including characters, integers,floating point values,
categorical data and more) in columns. It is similar to a spreadsheet,
a SQL table or the data.frame in R. Each column in a DataFrame is a Series.
"""
import pandas as pd
import numpy as np

message = 'DataFrame as a generalized NumPy array'
print(message.upper())
area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297,
             'Florida': 170312, 'Illinois': 149995}
area = pd.Series(area_dict)
print('Area of the each State:')
print(area)

# Now that we have this along with the population Series from before, we can 
# use a dictionary to construct a single two-dimensional object containing 
# this information:
population_dict = {'California': 38332521, 'Texas': 26448193, 
                   'New York': 19651127,
                   'Florida': 19552860,
                   'Illinois': 12882135}
population = pd.Series(population_dict)

states = pd.DataFrame({'population': population,'area': area})
print('Population and Area of each State:')
print(states)
print(states.index) #index attribute of the DataFrame
print(states.columns) #columns attribute of the DataFrame
print('')
print('') 
# Thus the DataFrame can be thought of as a generalization of a two-dimensional
# NumPy array, where both the rows and columns have a generalized index for 
# accessing the data.
print('')
message = 'DataFrame as Specialized Dictionary'
print(message.upper())
print(states['area'])
print('')
print('')
# =============================================================================
# Note: In a two-dimensional NumPy array,data[0] will return the first row.
# For a DataFrame, data['col0'] will return the first column. DataFrames 
# can be imagined as generalized dictionaries instead of generalized arrays.
# =============================================================================

message = 'Ways of Constructing DataFrame Objects'
print(message.upper())
print('Constructing DataFrame objects from a single Series object')
a = pd.DataFrame(population, columns=['population'])
print(a)

print('Constructing DataFrame objects from a list of Dicts')
data = [{'a': i, 'b': 2 * i} for i in range(3)]
b = pd.DataFrame(data)
print(b)

# =============================================================================
# Note: Even if some keys in the dictionary are missing, Pandas will fill them  
# in with NaN (i.e., “not a number”) values:
# =============================================================================
print('Constructing DataFrame Objects with a Nan Values')
c = pd.DataFrame([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}])
print(c)

print('Constructing DataFrame objects from Dictionary of Series Objects')
# As we saw before, a DataFrame can be constructed
# from a dictionary of Series objects as well:
d = pd.DataFrame({'population': population,
                  'area': area})
print(d)

print('Constructing DataFrame object from a two-dimensional NumPy array')
e = pd.DataFrame(np.random.rand(3, 2),
             columns=['foo', 'bar'],
             index=['a', 'b', 'c'])
print(e)

print('Constructing DataFrame object from a two-dimensional NumPy array')
A = np.zeros(3, dtype=[('A', 'i8'), ('B', 'f8')])
print('Structured Array: ', A,',' , A.dtype)
B = pd.DataFrame(A)
print('Obtained DataFrame: ')
print(B)