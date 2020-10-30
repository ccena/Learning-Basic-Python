# -*- coding: utf-8 -*-
"""
Pandas treats None and NaN as essentially interchangeable for indicating
missing or null values. There are several useful methods for detecting, removing,
and replacing null values in Pandas data structures. They are:
isnull()
        Generate a Boolean mask indicating missing values
notnull()
        Opposite of isnull()
dropna()
        Return a filtered version of the data
fillna()
        Return a copy of the data with missing values filled or imputed
"""
import pandas as pd
import numpy as np

message = 'Detecting null values'
print(message.upper())
data = pd.Series([1, np.nan, 'hello', None])
print(data.isnull())
print('')
# Boolean masks can be used directly as a Series or DataFrame index:
print('Boolean Masks as Series or DataFrame index:')
print(data[data.notnull()])
# The isnull() and notnull() methods produce similar Boolean results for DataFrames.
print('')
print('')

message = 'Dropping null values'
print(message.upper())
# In addition to the masking used before, there are the convenience methods, 
# dropna() (which removes NA values) and fillna() (which fills in NA values).
print('Removing NA values in a Series:')
print(data.dropna())
print('')
print('Removing NA values in a DataFrame:')
df = pd.DataFrame([[1, np.nan, 2],[2, 3, 5],[np.nan, 4, 6]])
print('DataFrame:')
print(df)
print('By default, dropna() will drop all rows in which any null value is present:')
print(df.dropna())

#Alternatively, you can drop NA values along a different axis; axis=1 drops 
# all columns containing a null value:
print("Using dropna(axis='columns') will drop all columns containing a null value: ")
print(df.dropna(axis=1))


# But this drops some good data as well; you might rather be interested in
# dropping rows or columns with all NA values, or a majority of NA values.
print('Using how and thresh parameters')
df[3] = np.nan
print('DataFrame:')
print(df)
# The default is how='any', such that any row or column (depending on the axis 
# keyword) containing a null value will be dropped.
print('Dropping the column containing all NA values:')
print(df.dropna(axis='columns', how='all'))
print('')
# For finer-grained control, the thresh parameter lets you specify a minimum
# number of non-null values for the row/column to be kept:
print('Removing 3 NA values in the rows')
print(df.dropna(axis='rows', thresh=3))
message = 'Here the first and last row have been dropped, because they contain' 
message += ' only two nonnull values.'
print(message)
print('')

print('Filling Null values')
data = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'))
print('Series Data:')
print(data)
print('Using data.fillna()) to replace NA entries in the Series with zero:')
print(data.fillna(0))

print('Using forward fill method will propagate the previous value forward:')
print(data.fillna(method='ffill'))
print('Using backward  fill method will propagate the next values backward:')
print(data.fillna(method='bfill'))

print('The forward and back fill methods apply on DataFrames, and allows us to specify the axis')
print('DataFrame:')
print(df)

print('Using forward fill method and axis = 1 will move the values to the right:')
print(df.fillna(method='fsfill', axis=1))

# =============================================================================
# Notice that if a previous value is not available during a forward fill, the
# NA value remains.
# =============================================================================


