# -*- coding: utf-8 -*-
"""
When you are performing operations between a DataFrame and a Series, the index
and column alignment is similarly maintained. Operations between a DataFrame 
and a Series are similar to operations between a two-dimensional and 
one-dimensional NumPy array.
"""

import pandas as pd
import numpy as np

rng = np.random.RandomState(42)
A = rng.randint(10, size=(3, 4))
print('Array A:')
print(A)
print('Subtracting A and A[0]:')
print(A - A[0])
print('Creating a DataFrame of A called df: ')
df = pd.DataFrame(A, columns=list('QRST'))
print(df)
print('Row Subtraction of df and df.iloc[0]:') #df.iloc[0] gives the first row 
# values
print(df.subtract(df.iloc[0])) #df-df.iloc[0]

# If you would instead like to operate column-wise, you can use the object .
# methods mentioned earlier, while specifying the axis keyword:

print('Column Subtraction of df with the R values:')
print(df.subtract(df['R'], axis=0))
print('')
# Note that these DataFrame/Series operations, will automatically align 
# indices between the two elements:
print('Automatic Aligning of Elements') 
halfrow = df.iloc[0, ::2]
print(halfrow)
print('')
print('df - halfrow:')
print(df - halfrow)
# This preservation and alignment of indices and columns means that operations
# on data in Pandas will always maintain the data context preventing error 
# when working with heterogeneous and misaligned data in raw Numpy arrays
