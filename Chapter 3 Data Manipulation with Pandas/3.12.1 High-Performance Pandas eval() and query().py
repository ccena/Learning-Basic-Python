# -*- coding: utf-8 -*-
"""
Pandas includes some experimental tools that allow you to directly access 
C-speed operations without costly allocation of intermediate arrays. These are
the eval() and query() functions 
"""

import pandas as pd
import numpy as np

print('Operations supported by pd.eval():')
# The eval() function in Pandas uses string expressions to efficiently 
# compute operations using DataFrames.
nrows, ncols = 100000, 100
rng = np.random.RandomState(42)
df1, df2, df3, df4, df5 = (pd.DataFrame(rng.randint(0, 1000, (100, 3)))
                           for i in range(5))

print('Arithmetic Operators')
#pd.eval() supports all arithmetic operators
result1 = -df1 * df2 / (df3 + df4) - df5
result2 = pd.eval('-df1 * df2 / (df3 + df4) - df5')
print(np.allclose(result1, result2)); print('')

print('Comparison operators')
# pd.eval() supports all comparison operators, including chained expressions
result1 = (df1 < df2) & (df2 <= df3) & (df3 != df4)
result2 = pd.eval('df1 < df2 <= df3 != df4')
print(np.allclose(result1, result2)); print('')

print('Bitwise operators')
# pd.eval() supports the & and | bitwise operators
result1 = (df1 < 0.5) & (df2 < 0.5) | (df3 < df4)
result2 = pd.eval('(df1 < 0.5) & (df2 < 0.5) | (df3 < df4)')
print(np.allclose(result1, result2)); print('')

print('Literal "and" & "or" in Bolean Expression')
# it also supports the use of the literal and and or in Boolean expressions:
result3 = pd.eval('(df1 < 0.5) and (df2 < 0.5) or (df3 < df4)')
print(np.allclose(result1, result3)); print('')

print('Object attributes and indices')
# pd.eval() supports access to object attributes via the
# obj.attr syntax, and indexes via the obj[index]
result1 = df2.T[0] + df3.iloc[1]
result2 = pd.eval('df2.T[0] + df3.iloc[1]')
print(np.allclose(result1, result2))
