# -*- coding: utf-8 -*-
"""
The way in which Pandas handles missing values is constrained by its reliance 
on the NumPy package, which does not have a built-in notion of NA values for 
nonfloating-point data types.
"""
import numpy as np
import pandas as pd

message = 'Pandas chose to use sentinels for missing data, and further chose'
message += 'use two already-existing \nPython null values: the special floating' 
message += 'point NaN value, and the Python None object.'
print(message)

print('None: Pythonic missing data')
vals1 = np.array([1, None, 3, 4])
print(vals1)

# for dtype in ['object', 'int']:
#     print("dtype =", dtype)
#     %timeit np.arange(1E6, dtype=dtype).sum()
#     print()
# The whole array is considered as a dtype=object which performs much slower 
# than the typically fast operations

# print(vals1.sum())
# This reflects the fact that addition between an integer and None is undefined.


print('NaN: Missing numerical data')
vals2 = np.array([1, np.nan, 3, 4])
print(vals2.dtype) #The array is labeled as a float64
print(1 + np.nan)
print(0 * np.nan)
print(vals2.sum(), vals2.min(), vals2.max())
print(np.nansum(vals2), np.nanmin(vals2), np.nanmax(vals2))
print('')

print('NaN and None in Pandas:')
# NaN and None both have their place, and Pandas is built to handle the two 
# of them nearly interchangeably, converting between them where appropriate:
df = pd.Series([1, np.nan, 2, None])
print(df) #As printed, the value None is converted to Nan
print('')

x = pd.Series(range(2), dtype=int)
print('Series: ')
print(x)
x[0] = None
print('Setting x[0] = None yields:')
print(x)
# Notice that in addition to casting the integer array to floating point, 
# Pandas automatically converts the None to a NaN value.

# =============================================================================
# Keep in mind that in Pandas, string data is always stored with an object dtype.
# =============================================================================
