# -*- coding: utf-8 -*-
"""
Just as Pandas has a top-level pd.eval() function, DataFrames have an eval()
method that works in similar ways. The benefit of the eval() method is that 
columns can be referred to by name.
"""

import pandas as pd
import numpy as np

rng = np.random.RandomState(42)
df = pd.DataFrame(rng.rand(1000, 3), columns=['A', 'B', 'C'])
print(df.head())

# Using pd.eval() to compute expressions with the three columns
print('The pd.eval() can be used to compute expressions with the 3 columns:')
result1 = (df['A'] + df['B']) / (df['C'] - 1)
result2 = pd.eval("(df.A + df.B) / (df.C - 1)")
print(result1)
print(np.allclose(result1, result2)); print('')

print('The df.eval allows much more compact evaluation with the columns:')
result3 = df.eval('(A + B) / (C - 1)')
print(np.allclose(result1, result3)); print('')

print('Assignment in DataFrame.eval()')
print('data:'); print(df.head())
df.eval('D = (A + B) / C', inplace=True)
print('Creating a New Column with df.eval():'); print(df.head())
print('Modifying the New Column:')
df.eval('D = (A - B) / C', inplace=True)
print(df.head()); print('')

print('Local variables in DataFrame.eval()')
column_mean = df.mean(axis=1)
result1 = df['A'] + column_mean
result2 = df.eval('A + @column_mean')
print(result2.head)
print(np.allclose(result1, result2))


