# -*- coding: utf-8 -*-
"""
Pandas includes features to address both this need for vectorized string 
operations and for correctly handling missing data via the str attribute of 
Pandas Series and Index objects containing strings.
"""
import pandas as pd
import numpy as np

print('Introducing Pandas String Operations')
x = np.array([2, 3, 5, 7, 11, 13])
print('Example of scalar operation, x*2 =', x * 2)
data = ['peter', 'Paul', 'MARY', 'gUIDO']
print('raw data:', data)
print('Corrected data capitalization: ', [s.capitalize() for s in data]) 
#this syntax will break if there are missing values in the array

#this can be remedied by doing the following:
names = pd.Series(data)
print('Names:'); print(names)
names = names.str.capitalize() #corrects the capitalization of the entries
print('Corrected data capitalization: ')
print(names)

