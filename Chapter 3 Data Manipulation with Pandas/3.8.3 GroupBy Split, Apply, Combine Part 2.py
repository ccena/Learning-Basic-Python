# -*- coding: utf-8 -*-
"""
In the simple examples presented before, we split the DataFrame on a single 
column name. This is just one of many options by which the groups can be 
defined, and we’ll go through some other options for group specification here.
"""
import pandas as pd
import numpy as np
import seaborn as sns

rng = np.random.RandomState(0)
df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'data1': range(6),
                   'data2': rng.randint(0, 10, 6)},
                  columns = ['key', 'data1', 'data2'])

print('A list, array, series, or index providing the grouping keys:')
# The key can be any series or list
# with a length matching that of the DataFrame.
L = [0, 1, 0, 1, 2, 0] #This will replace the value for the keys
print('df:'); print(df); 
print('Summing L and df:'); print(df.groupby(L).sum()); print('')
# Of course, this means there’s another, more verbose way of accomplishing the
# df.groupby('key') from before:
print('df:'); print(df); 
print('Sum by keys:'); print(df.groupby(df['key']).sum()) ; print('')

print('A dictionary or series mapping index to group')
# Another method is to provide a dictionary
# that maps index values to the group keys:
df2 = df.set_index('key')
mapping = {'A': 'vowel', 'B': 'consonant', 'C': 'consonant'}
print('df2: '); print(df2); print(df2.groupby(mapping).sum())
#Now the result has 2 keys, consonant and vowel
print('')

print('Passing any Python function to groupby')
# Similar to mapping, you can pass any Python function that will
# input the index value and output the group:
print('Data: '); print(df2);
print('Calculating the Mean and Formatting the Indices:')
print(df2.groupby(str.lower).mean()); print('')

print('A list of valid keys')
# Further, any of the preceding key choices can be combined to
# group on a multi-index:
print(df2.groupby([str.lower, mapping]).mean()); print('')

print('Grouping example on Planets')
planets = sns.load_dataset('planets')
print(planets.shape)
print(planets.head()); print('')
decade = 10 * (planets['year'] // 10)
decade = decade.astype(str) + 's'
decade.name = 'decade'
planets.groupby(['method', decade])['number'].sum().unstack().fillna(0)



    


