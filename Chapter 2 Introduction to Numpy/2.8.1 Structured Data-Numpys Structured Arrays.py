# -*- coding: utf-8 -*-
"""
While often our data can be well represented by a homogeneous array of values,
sometimes this is not the case. This section demonstrates the use of NumPy’s 
structured arrays and record arrays, which provide efficient storage for 
compound, heterogeneous data. While the patterns shown here are useful for 
simple operations, scenarios like this often lend themselves to the use of 
Pandas DataFrames.     
"""

import numpy as np

# Imagine that we have several categories of data on a number of people (say, 
# name, age, and weight), and we’d like to store these values for use in a 
# Python program. It would be possible to store these in three separate arrays:
name = ['Alice', 'Bob', 'Cathy', 'Doug']
age = [25, 45, 37, 19]
weight = [55.0, 85.5, 68.0, 61.5]

# NumPy can handle this through structured arrays, which are.
# arrays with compound data types.
print('Creating a structured array using a compound data type:')   
data = np.zeros(4, dtype={'names':('name', 'age', 'weight'),
                          'formats':('U10', 'i4', 'f8')})
# Here 'U10' = “Unicode string of maximum length 10,” 
# 'i4' = “4-byte (i.e., 32 bit) integer,” 
# 'f8' = “8-byte (i.e., 64 bit) float.”
print(data.dtype)
print('')

# Now that we’ve created an empty container array, we can fill the array with
# our lists of values:
print('Placing Values in the empty structured array:')
data['name'] = name
data['age'] = age
data['weight'] = weight
print(data)
print('')
# The handy thing with structured arrays is that you can now refer to values 
# either by index or by name:
print('All names on data: ', data['name'])
print('First row of data: ', data[0])
print('Name from the last row: ', data[-1]['name'])
print('Names with age under 30: ', data[data['age'] < 30]['name'])