# -*- coding: utf-8 -*-
"""
Series and DataFrames are built with merging and joining data operation 
in mind, and Pandas includes functions and methods
that make this sort of data wrangling fast and straightforward.
"""
import pandas as pd
import numpy as np

def make_df(cols, ind):
    """Quickly make a DataFrame"""
    data = {c: [str(c) + str(i) for i in ind] for c in cols}
    return pd.DataFrame(data, ind)
# example DataFrame
a = make_df('ABC', range(3))
print( 'Data:')
print(a)

print('Concatenation of Numpy Arrays')
x = [1, 2, 3]
print('x: ', x)
y = [4, 5, 6]
print('y: ', y)
z = [7, 8, 9]
print('z: ', z)
print('Combining x y and z: ', np.concatenate([x, y, z]))
b = [[1, 2],[3, 4]]
print('b:', b)
print('Concatenating b with itself: ')
print(np.concatenate([b, b], axis=1))