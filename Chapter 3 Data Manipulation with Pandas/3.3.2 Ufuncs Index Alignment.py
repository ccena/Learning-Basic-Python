# -*- coding: utf-8 -*-
"""
For binary operations on two Series or DataFrame objects, Pandas will align
indices in the process of performing the operation. This is very convenient
when you are working with incomplete data
"""


import pandas as pd
import numpy as np
rng = np.random.RandomState(42)


print('Index alignment in Series')
area = pd.Series({'Alaska': 1723337, 'Texas': 695662,
                  'California': 423967}, name='area')
population = pd.Series({'California': 38332521, 'Texas': 26448193,
                        'New York': 19651127}, name='population')
print('Dividing the population with the area:')
print(population/area) 
print('')
# The resulting array contains the union of indices of the two input arrays
print('The union of the indices: ', area.index | population.index)
A = pd.Series([2, 4, 6], index=[0, 1, 2])
B = pd.Series([1, 3, 5], index=[1, 2, 3])
print('Adding A and B:')
print(A+B)
#To remove the Nan, we can modify the fill value using
# appropriate object methods in place of the operators.
print('Adding A and B while removing Nan:')
print(A.add(B, fill_value=0))
print('')

print('Index Alignment in DataFrame A:')
A = pd.DataFrame(rng.randint(0, 20, (2, 2)), 
                 columns=list('AB'))
print('A:')
print(A)
print('Index Alignment in DataFrame B: ')
B = pd.DataFrame(rng.randint(0, 10, (3, 3)), 
                 columns=list('BAC'))
print('B: ')
print(B)
print('Adding A and B:')
print(A+B)
# Notice that indices are aligned correctly irrespective of their order in the 
# two objects, and indices in the result are sorted.
print('Adding A and B while removing Nan:')
fill = A.stack().mean() #The fill value will be the mean of A
print(A.add(B, fill_value=fill)) #The fill value is added to the other values
#thereby removing the Nan 
