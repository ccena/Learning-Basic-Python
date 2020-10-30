# -*- coding: utf-8 -*-
"""
The pd.merge() provides a variety of options for handling column names 
that do not match so nicely. 
"""

import pandas as pd

print('The on keyword')
# One can explicitly specify the name of the key column using the on keyword,
# which takes a column name or a list of column names:

df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
'group': ['Accounting', 'Engineering', 'Engineering', 'HR']})
df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake', 'Sue'],
'hire_date': [2004, 2008, 2012, 2014]})
print('df1:'); print(df1); print('df2:'); print(df2)
df3 = pd.merge(df1, df2, on='employee')
print('Creating df3 by combining df1 and df2:')
print(df3)
print('')
# This option works only if both the left and right DataFrames have the 
# specified column name.

print('The left_on and right_on keywords')
df4 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
'salary': [70000, 80000, 120000, 90000]})
print('df1:'); print(df1); print('df4:'); print(df4)
df5 = pd.merge(df1, df4, left_on="employee", right_on="name")
print('Creating df5 by combining df1 and df4:')
print(df5)
# The result has a redundant column that we can drop if desired—for example, by
# using the drop() method of DataFrames:
print('Removing the name column in df5 using drop():')
df6 = pd.merge(df1, df4, left_on="employee", right_on="name").drop('name', axis=1)
print(df6)
print('')

print('The left_index and right_index keywords')
# Sometimes, rather than merging on a column, you would instead like to merge 
# on an index.
df1a = df1.set_index('employee')
df2a = df2.set_index('employee')
print('df1a:'); print(df1a); print('df2a:'); print(df2a)
# You can use the index as the key for merging by specifying the left_index
# and/or right_index flags in pd.merge():
print('Combining df1 and df2 using the index as keys: ')
print(pd.merge(df1a, df2a, left_index=True, right_index=True))
print('')

# For convenience, DataFrames implement the join() method, which performs a
# merge that defaults to joining on indices:
print('Instead of specifying the index, one can simply use join():')
print(df1a.join(df2a))    
print('')

# If you’d like to mix indices and columns, you can combine left_index with
# right_on or left_on with right_index to get the desired behavior:
print('Mixing indices and columns:')
print('df1:'); print(df1); print('df4:'); print(df4)
print('df7:')
df7 = pd.merge(df1a, df4, left_index=True, right_on='name')
print(df7) 
    

    
    
    
    