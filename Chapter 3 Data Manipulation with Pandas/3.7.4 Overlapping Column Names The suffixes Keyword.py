# -*- coding: utf-8 -*-
"""
Finally, you may end up in a case where your two input DataFrames have conflicting
column names.
"""

import pandas as pd
df8 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'rank': [1, 2, 3, 4]})

df9 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
'rank': [3, 1, 4, 2]})
print('df8:'); print(df8);print('df9:'); print(df9); print('df10: ')
df10 = pd.merge(df8, df9, on="name")
print(df10)
# Because the output would have two conflicting column names, the merge function
# automatically appends a suffix _x or _y to make the output columns unique.
print('')
# If these defaults are inappropriate, it is possible to specify a custom suffix
# using the suffixes keyword:
df10 = pd.merge(df8, df9, on="name", suffixes=["_L", "_R"])    
print('Changing the suffix for the rank:')
print(df10)
# These suffixes work in any of the possible join patterns, and work also if there are
# multiple overlapping columns.


     
